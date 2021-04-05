<template>
    <b-form @submit="goSave($event)">
        <div class="form__item">
            <span class="form__label">Номер телефона</span>
            <div class="form__control">
                    {{users.item.phone}}
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Никнейм</span>
            <div class="form__control">
                {{users.item.username}}
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Страна</span>
            <div class="form__control">
                {{users.item.country.name_ru}}
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Образование</span>
            <div class="form__control">
                {{users.item.education.name_ru}}
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Сфера деятельности</span>
            <div class="form__control">
                {{users.item.action_area.name_ru}}
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Языки</span>
            <div class="form__control">
                {{users.item.country.name_ru}}
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Семья</span>
            <div class="form__control">
                {{users.item.family}}
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Пол</span>
            <div class="form__control">
                {{users.item.sex}}
            </div>
        </div>
        <div class="form__item">
            <span class="form__label">Доступ к телефонной книге</span>
            <div class="form__control">
                {{users.item.mobile_book_access}}
            </div>
        </div>
    </b-form>
</template>

<script>
import { mapState } from 'vuex'
import Vue from "vue";

export default {
    name: 'UserForm',

    data () {
        return {
            id: this.$route.params.id,
            alert: false
        }
    },
    created() {
        if (this.id){
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Пользователи', to: {name: 'students'}},
                {text: 'Редактировать', to: {name: 'student-update', params: {id: this.id}}}
            ];
        }else{
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Пользователи', to: {name: 'students'}},
                {text: 'Создать', to: {name: 'student-create'}}
            ];
        }
        if (this.id) {
            this.$store.dispatch('users/getItem', this.id)
                .then(item => {
                    console.log(item)
                })
                .catch(error => {
                    console.log(error)
                });
        }
    },
    computed: {
        ...mapState(['users']),
    },
    methods: {
        processFile(event) {
            this.user.item.image = event[0]
        },
        goSave($event){
            
            $event.preventDefault();
            let data = Object.assign({}, this.users.item);
            data.id = this.id
            data.image = this.users.image;

            this.$store.dispatch('users/saveItem', data)
                .then(item => {
                    console.log(item)
                    Vue.templateShowSuccess();
                    if(!data.id) Vue.goBack();
                    else this.$store.dispatch('users/getItem', this.id)
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
        deleteImg() {
            let confirmDelete = confirm('Удалить фото?');
            if (confirmDelete) {
                this.users.avatar = null;
                this.users.item.avatar = null;
            }
        } 
    },
}
</script>

<style scoped>

</style>
