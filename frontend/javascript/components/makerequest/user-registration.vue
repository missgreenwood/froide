<template>
  <div>
    <div class="card mb-3">
      <div class="card-body">
        <div class="form-group row">
          <label
            for="id_user_email"
            class="col-sm-3 col-form-label"
            :class="{
              'text-danger': errors.user_email,
              'field-required': !user
            }">
            {{ i18n.yourEmail }}
          </label>
          <div class="col-sm-9">
            <p v-if="user" id="email_address" class="form-control-plaintext">
              {{ user.email }}
            </p>
            <div v-else>
              <input
                v-model="email"
                type="email"
                name="user_email"
                class="form-control"
                :class="{ 'is-invalid': errors.user_email }"
                :placeholder="formFields.user_email.placeholder"
                required />
              <p
                v-for="e in errors.user_email"
                :key="e.message"
                class="text-danger">
                {{ e.message }}
              </p>
            </div>
          </div>
        </div>

        <div class="form-group row">
          <label
            for="id_address"
            class="col-sm-3 col-form-label"
            :class="{
              'text-danger': errors.address,
              'field-required': requiresPostalAddress
            }">
            {{ i18n.yourAddress }}
          </label>
          <div class="col-sm-9">
            <div>
              <textarea
                v-model="address"
                name="address"
                class="form-control"
                :class="{ 'is-invalid': errors.address }"
                :placeholder="formFields.address.placeholder"
                :required="requiresPostalAddress" />
              <p v-for="e in errors.address" :key="e.message">
                {{ e.message }}
              </p>
              <p class="help-block">
                <span v-html="addressHelpText" />
              </p>
            </div>
          </div>
        </div>
        <template v-if="formFields.time">
          <input type="hidden" name="time" :value="formFields.time.initial" />
        </template>
        <template v-if="formFields.phone">
          <div class="form-group row d-none honigtopf">
            <label class="col-lg-3 col-form-label" for="id_phone">
              {{ formFields.phone.label }}
            </label>
            <div class="col-lg-9">
              <input
                id="id_phone"
                class="form-control"
                type="text"
                name="phone" />
            </div>
          </div>
        </template>
        <template v-if="formFields.test">
          <div class="form-group row">
            <label
              class="col-lg-3 col-form-label"
              :class="{
                'text-danger': errors.test,
                'field-required': formFields.test.required
              }"
              for="id_test">
              {{ formFields.test.label }}
            </label>
            <div class="col-lg-9">
              <input class="form-control" type="text" required name="test" />
              <p class="help-block">
                <span>{{ formFields.test.help_text }}</span>
              </p>
            </div>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import I18nMixin from '../../lib/i18n-mixin'

export default {
  name: 'UserRegistration',
  mixins: [I18nMixin],
  props: {
    config: {
      type: Object
    },
    form: {
      type: Object
    },
    user: {
      type: Object,
      default: null
    },
    defaultLaw: {
      type: Object
    },
    initialEmail: {
      type: String,
      default: ''
    },
    initialAddress: {
      type: String,
      default: ''
    },
    initialPrivate: {
      type: Boolean,
      default: false
    },
    addressHelpText: {
      type: String,
      default: null
    },
    addressRequired: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      emailValue: this.initialEmail,
      addressValue:
        this.initialAddress || (this.user && this.user.address) || ''
    }
  },
  computed: {
    formFields() {
      return this.form.fields
    },
    errors() {
      if (this.form) {
        return this.form.errors
      }
      return {}
    },
    addressHelpTextValue() {
      if (this.addressHelpText !== null) {
        return this.addressHelpText
      }
      return this.formFields.address.help_text
    },
    email: {
      get() {
        return this.emailValue
      },
      set(value) {
        this.emailValue = value
        this.$emit('update:initialEmail', value)
      }
    },
    address: {
      get() {
        return this.addressValue
      },
      set(value) {
        this.addressValue = value
        this.$emit('update:initialAddress', value)
      }
    },
    requiresPostalAddress() {
      if (this.addressRequired) {
        return true
      }
      if (this.defaultLaw) {
        return !this.defaultLaw.email_only
      }
      return true
    }
  }
}
</script>
