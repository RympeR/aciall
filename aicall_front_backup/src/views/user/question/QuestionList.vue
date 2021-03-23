<template>
    <b-row>
        <b-col>
            <div class="mb-4">
                <b-button :to="{name: 'question-create'}" variant="primary" size="md">
                    Добавить
                </b-button>
            </div>
            <b-table hover outlined head-variant="light"
                :items="question.list"
                :fields="fields"
                :filter="filter"
                >
                <template #cell(index)="data">
                    <b>{{ data.index + 1 }}</b>
                </template>
                <template v-slot:cell(actions)="data">
                    <div class="table__actions">
                        <b-button class="btn_edit" :to="{name: 'question-update', params: {id: data.item.id}}"></b-button>
                        <!--<btn-turn :turn="true"/>-->
                        <b-button class="btn_delete" @click="deleteQuestion(data.item.id)"/>
                    </div>
                </template>
            </b-table>
        </b-col>
    </b-row>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: "QuestionList",
    data () {
        return {
            fields: [
                { key: 'index', label: '#'},
                { key: 'id', label: 'ID'},
                { key: 'name_ru', label: 'Название ru', sortable: true},
                { key: 'name_eng', label: 'Название eng', sortable: true},
                { key: 'actions', label: ''},

            ],
            activePage: 1,
            filter: {
                level: null
            },
        }
    },
    computed: {
        ...mapState(['question']),
    },
    methods: {
        ...mapActions({
                saveQuestion: 'question/saveItem',
                deleteQuestion: 'question/deleteItem',
                getQuestions: 'question/getList'
            })
    },
    created() {
        this.$store.state.breadcrumbs = [
            {text: 'Главная', to: {name: 'home'}},
            {text: 'Вопросы', to: {name: 'questions'}},
        ];
        this.getQuestions().then(list => {
                console.log(list)
        })
        .catch(error => {
            console.log(error)
        });
    }
}
</script>

<style scoped>

</style>
