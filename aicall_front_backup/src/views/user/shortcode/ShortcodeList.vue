<template>
    <b-row>
        <b-col>

            <b-table hover outlined head-variant="light"
                :items="shortcode.list"
                :fields="fields"
                :filter="filter"
                >
                <template #cell(index)="data">
                    <b>{{ data.index + 1 }}</b>
                </template>
                <template v-slot:cell(actions)="data">
                    <div class="table__actions">
                        <b-button class="btn_edit" :to="{name: 'shortcode-update', params: {id: data.item.id}}"></b-button>
                        <!--<btn-turn :turn="true"/>-->
                        <b-button class="btn_delete" @click="deleteShortcode(data.item.id)"/>
                    </div>
                </template>
            </b-table>
        </b-col>
    </b-row>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: "ShortcodeList",
    data () {
        return {
            fields: [
                { key: 'index', label: '#'},
                { key: 'id', label: 'ID'},
                { key: 'shortcode', label: 'Шорткод', sortable: true},
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
        ...mapState(['shortcode']),
    },
    methods: {
        ...mapActions({
                saveShortcode: 'shortcode/saveItem',
                deleteShortcode: 'shortcode/deleteItem',
                getShortcodes: 'shortcode/getList'
            })
    },
    created() {
        this.$store.state.breadcrumbs = [
            {text: 'Главная', to: {name: 'home'}},
            {text: 'Психотипы', to: {name: 'shortcodes'}},
        ];
        this.getShortcodes().then(list => {
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
