<template>
    <b-form @submit="goSave">
        <b-tabs content-class="mt-3">
            <b-tab title="Основное" active>
            <div class="form__item">
                <span class="form__label">Название ru</span>
                <div class="form__control">
                    <div class="row">
                        <div class="col-12">
                            <b-form-input class="short"
                                          type="text"
                                          required
                                          v-model="negative_sides.item.name_ru"
                            />
                        </div>
                    </div>
                </div>
            </div>
            <div class="form__item">
                <span class="form__label">Название eng</span>
                <div class="form__control">
                    <div class="row">
                        <div class="col-12">
                            <b-form-input class="short"
                                          type="text"
                                          required
                                          v-model="negative_sides.item.name_eng"
                            />
                        </div>
                    </div>
                </div>
            </div>

           
            </b-tab>

        </b-tabs>

        <div class="form__item form__item_submit">
            <div class="form__control">
                <b-button type="submit" variant="primary">Сохранить</b-button>
            </div>
        </div>
    </b-form>
</template>

<script>
import { mapState } from 'vuex'
import Vue from "vue";

export default {
    name: 'NegativeSidesForm',
    components: {
        
    },
    data () {
        return {
            id: this.$route.params.id,
            alert: false
        }
    },
    computed: {
        ...mapState(['negative_sides']),
    },
    created() {
        if (this.id){
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Негативные стороны', to: {name: 'negative-sides'}},
                {text: 'Редактировать', to: {name: 'negative-sides-update', params: {id: this.id}}}
            ];
        }else{
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Негативные стороны', to: {name: 'negative-sides'}},
                {text: 'Создать', to: {name: 'negative-sides-create'}}
            ];
        }
        if (this.$route.params.id) {
            this.$store.dispatch('negative_sides/getItem', this.$route.params.id)
                .then(item => {
                    console.log(item)
                })
                .catch(error => {
                    console.log(error)
                });
        }
    },
    methods: {
        goSave(e){
            e.preventDefault();
            let data = Object.assign({}, this.negative_sides.item);
            data.id = this.id
            this.$store.dispatch('negative_sides/saveItem',data)
                .then(item => {
                    console.log(item)
                    Vue.templateShowSuccess();
                    if(!data.id) Vue.goBack();
                    else this.$store.dispatch('negative_sides/getItem', this.$route.params.id)
                            .then(item => {
                                console.log(item)
                            })
                            .catch(error => {
                                console.log(error)
                            });
                })
                .catch(error => {
                    console.log(error)
                });
        },
    },
}
</script>

<style scoped>

</style>
