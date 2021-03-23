<template>
    <b-form @submit="goSave($event)">
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
                                v-model="talktheme.item.name_ru"
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
                                v-model="talktheme.item.name_eng"
                            />
                        </div>
                    </div>
                </div>
            </div>
            <div class="form__item">
                <span class="form__label">Изображение png</span>
                <div class="form__control">
                    <template v-if="talktheme.item.image_png">
                        <div class="img__thumbnail">
                            <div class="img__thumbnail-img">
                                <b-img :id="`field-${talktheme.item.id}`"
                                       :src="talktheme.item.image_png" width="80"
                                       v-b-modal="'modal__thumbnail' + talktheme.item.id"
                                />
                            </div>
                            <b-modal :id="'modal__thumbnail' + talktheme.item.container_id" scrollable hide-footer centered class="modal-dialog-auto">
                                <b-img :src="talktheme.item.image_png" fluid/>
                            </b-modal>
                            <b-button type="button" class="media-delete" variant="link" @click="deleteImgPng">Удалить</b-button>
                        </div>
                    </template>
                    <template v-else>
                        <b-form-file
                            :id="`field-${talktheme.image_png}`"
                            v-model="talktheme.image_png"
                            plain
                        />
                    </template>
                </div>
            </div>

            <div class="form__item">
                <span class="form__label">Изображение svg</span>
                <div class="form__control">
                    <template v-if="talktheme.item.image_svg">
                        <div class="img__thumbnail">
                            <div class="img__thumbnail-img">
                                <b-img :id="`field-${talktheme.item.id}`"
                                       :src="talktheme.item.image_svg" width="80"
                                       v-b-modal="'modal__thumbnail' + talktheme.item.id"
                                />
                            </div>
                            <b-modal :id="'modal__thumbnail' + talktheme.item.id" scrollable hide-footer centered class="modal-dialog-auto">
                                <b-img :src="talktheme.item.image_svg" fluid/>
                            </b-modal>
                            <b-button type="button" class="media-delete" variant="link" @click="deleteImgSvg">Удалить</b-button>
                        </div>
                    </template>
                    <template v-else>
                        <b-form-file
                            :id="`field-${talktheme.image_svg}`"
                            v-model="talktheme.image_svg"
                            plain
                        />
                    </template>
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
    name: 'TalkThemeForm',
    components: {
        
    },
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
                {text: 'Тема для разговора', to: {name: 'talkthemes'}},
                {text: 'Редактировать', to: {name: 'talktheme-update', params: {id: this.id}}}
            ];
        }else{
            this.$store.state.breadcrumbs = [
                {text: 'Главная', to: {name: 'home'}},
                {text: 'Тема для разговора', to: {name: 'talkthemes'}},
                {text: 'Создать', to: {name: 'talktheme-create'}}
            ];
        }
        if (this.id) {
            this.$store.dispatch('talktheme/getItem', this.id)
                .then(item => {
                    console.log(item)
                })
                .catch(error => {
                    console.log(error)
                });
        }
    },
    computed: {
        ...mapState(['talktheme']),
    },
    methods: {
        processFile(event) {
            console.log('Event: ', event);
            this.talktheme.item.image_png = event[0]
            this.talktheme.item.image_svg = event[1]
        },
        goSave($event){
            $event.preventDefault();
            
            let data = Object.assign({}, this.talktheme.item);
            data.id = this.id
            data.image_png = this.talktheme.image_png;
            data.image_svg = this.talktheme.image_svg;
            
            console.log(data);

            this.$store.dispatch('talktheme/saveItem', data)
                .then(item => {
                    console.log(item)
                    Vue.templateShowSuccess();
                    if(!data.id) Vue.goBack();
                    else this.$store.dispatch('talktheme/getItem', this.$route.params.id)
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
        deleteImgPng() {
            let confirmDelete = confirm('Удалить фото?');
            if (confirmDelete) {
                this.containers.image_png = null;
                this.containers.item.image_png = null;
            }
        },
        deleteImgSvg() {
            let confirmDelete = confirm('Удалить фото?');
            if (confirmDelete) {
                this.containers.image_svg = null;
                this.containers.item.image_svg = null;
            }
        },
    },
}
</script>

<style scoped>

</style>
