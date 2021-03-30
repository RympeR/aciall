<template>
  <b-form>
    <b-tabs content-class="mt-3">
      <b-tab title="Основное" active>
        <div class="form__item">
          <span class="form__label">Отправитель</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                <b-link
                  :to="{
                    name: 'student-update',
                    params: {
                      id: characteristics.item.sender.id,
                    },
                  }"
                  >{{ characteristics.item.sender.username }},
                  {{ characteristics.item.sender.phone }}</b-link
                >
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Получатель</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                <b-link
                  :to="{
                    name: 'student-update',
                    params: {
                      id: characteristics.item.reciever.id,
                    },
                  }"
                  >{{ characteristics.item.reciever.username }},
                  {{ characteristics.item.reciever.phone }}</b-link
                >
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Позитивные стороны</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                {{characteristics.item.positive_side}}
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Негативные стороны</span>
          <div class="form__control">
            <div class="row">
              <div class="col-6">
                {{characteristics.item.negative_side}}
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Рейтинг</span>
          <div class="form__control">
            <div class="row">
              <div class="col-12">
                {{characteristics.item.grade}}
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Имя для отправителя</span>
          <div class="form__control">
            <div class="row">
              <div class="col-12">
                {{characteristics.item.sender_name}}
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Имя для поулчателя</span>
          <div class="form__control">
            <div class="row">
              <div class="col-12">
                {{characteristics.item.reciever_name}}
              </div>
            </div>
          </div>
        </div>
        <div class="form__item">
          <span class="form__label">Совместиомсть</span>
          <div class="form__control">
            <div class="row">
              <div class="col-12">
                {{characteristics.item.compatible}}
              </div>
            </div>
          </div>
        </div>
        
      </b-tab>
    </b-tabs>
  </b-form>
</template>

<script>
import { mapState, mapActions } from "vuex";
import Vue from "vue";

export default {
  name: "CharacteristicsForm",
  components: {},
  data() {
    return {
      id: this.$route.params.id,
      alert: false,
    };
  },
  computed: {
    ...mapState([
      "characteristics",
      "users",
      "positive_sides",
      "negative_sides",
    ]),
  },
  created() {
    if (this.id) {
      this.$store.state.breadcrumbs = [
        { text: "Главная", to: { name: "home" } },
        { text: "Характеристики", to: { name: "characteristics" } },
        {
          text: "Редактировать",
          to: {
            name: "characteristics-update",
            params: { id: this.id },
          },
        },
      ];
    } else {
      this.$store.state.breadcrumbs = [
        { text: "Главная", to: { name: "home" } },
        { text: "Характеристики", to: { name: "characteristics" } },
        { text: "Создать", to: { name: "characteristics-create" } },
      ];
    }
    if (this.$route.params.id) {
      this.$store
        .dispatch("characteristics/getItem", this.$route.params.id)
        .then((item) => {
          console.log(item);
        })
        .catch((error) => {
          console.log(error);
        });
    }
    this.getPositiveSides().then((list) => {
      console.log(list);
    });
    this.positive_sides = this.positive_sides.join(", ");
    this.getNegativeSides().then((list) => {
        console.log(list);
    });
    this.negative_sides = this.negative_sides.join(", ");

    this.$store
      .dispatch("users/getList")
      .then((item) => {
        console.log(item);
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    ...mapActions({
      getPositiveSides: "positive_sides/getList",
      getNegativeSides: "negative_sides/getList",
      getUsers: "users/getList",
    }),
    goSave(e) {
      e.preventDefault();
      let data = Object.assign({}, this.characteristics.item);
      data.id = this.id;
      this.$store
        .dispatch("characteristics/saveItem", data)
        .then((item) => {
          console.log(item);
          Vue.templateShowSuccess();
          if (!data.id) Vue.goBack();
          else
            this.$store
              .dispatch("characteristics/getItem", this.$route.params.id)
              .then((item) => {
                console.log(item);
              })
              .catch((error) => {
                console.log(error);
              });
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped></style>
