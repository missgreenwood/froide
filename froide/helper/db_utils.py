from django.db import IntegrityError, models

from froide.helper.text_utils import slugify


def save_obj_with_slug(obj: models.Model, attribute: str = "title", **kwargs) -> None:
    obj.slug = slugify(getattr(obj, attribute))
    return save_obj_unique(obj, "slug", **kwargs)


def save_obj_unique(
    obj: models.Model,
    attr: str,
    count: int = 0,
    postfix_format: str = "-{count}",
) -> None:
    klass = obj.__class__
    MAX_COUNT = 10000  # max 10 thousand loops
    base_attr = getattr(obj, attr)
    initial_count = count
    first_round = count == 0
    postfix = ""
    while True:
        try:
            while count - initial_count < MAX_COUNT:
                if not first_round:
                    postfix = postfix_format.format(count=count)
                if not klass.objects.filter(
                    **{attr: getattr(obj, attr) + postfix}
                ).exists():
                    break
                if first_round:
                    first_round = False
                    count = max(
                        klass.objects.filter(
                            **{"%s__startswith" % attr: base_attr}
                        ).count(),
                        initial_count,
                    )
                else:
                    count += 1
            setattr(obj, attr, base_attr + postfix)
            obj.save()
        except IntegrityError:
            if count - initial_count < MAX_COUNT:
                if first_round:
                    first_round = False
                    count = max(
                        klass.objects.filter(
                            **{"%s__startswith" % attr: base_attr}
                        ).count(),
                        initial_count,
                    )
                count += 1
            else:
                raise
        else:
            break
