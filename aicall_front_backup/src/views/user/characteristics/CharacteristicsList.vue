<template>
    <b-row>
        <b-col>

            <b-table hover outlined head-variant="light"
                :items="characteristics.list"
                :fields="fields"
                :filter="filter"
                >
                <template #cell(index)="data">
                    <b>{{ data.index + 1 }}</b>
                </template>
                <template v-slot:cell(first_user_name)="data">
                    <div class="table__actions">
                        <b-link class="btn_edit" :to="{name: 'student-update', params: {id: data.item.sender.id}}">{{data.item.first_user_name}}</b-link>       
                    </div>
                </template>
                <template v-slot:cell(first_user_phone)="data">
                    <div class="table__actions">
                        <b-link class="btn_edit" :to="{name: 'student-update', params: {id: data.item.sender.id}}">{{data.item.first_user_phone}}</b-link>       
                    </div>
                </template>
                <template v-slot:cell(sec_user_name)="data">
                    <div class="table__actions">
                        <b-link class="btn_edit" :to="{name: 'student-update', params: {id: data.item.reciever.id}}">{{data.item.sec_user_name}}</b-link>       
                    </div>
                </template>
                <template v-slot:cell(sec_user_phone)="data">
                    <div class="table__actions">
                        <b-link class="btn_edit" :to="{name: 'student-update', params: {id: data.item.reciever.id}}">{{data.item.sec_user_phone}}</b-link>       
                    </div>
                </template>
                <template v-slot:cell(actions)="data">
                    <div class="table__actions">
                        <b-button class="btn_edit" :to="{name: 'characteristics-update', params: {id: data.item.id}}"></b-button>       
                    </div>
                </template>
            </b-table>
        </b-col>
    </b-row>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    name: "CharacteristicsList",
    data () {
        return {
            fields: [
                { key: 'index', label: '#'},
                { key: "id", label: "ID" },
				{ key: "first_user_name", label: "Отправитель имя" },
				{ key: "first_user_phone", label: "Отправитель телефон" },
				{ key: "sec_user_name", label: "Получатель имя" },
				{ key: "sec_user_phone", label: "Получатель телефон" },
				{ key: "positive_side", label: "Положительные стороны" },
				{ key: "negative_side", label: "Негативные стороны" },
				{ key: "reciever_name", label: "Имя для получателя"},
				{ key: "grade", label: "Рейтинг", sortable: true },
				{ key: "compatible", label: "Своместимы" },
                { key: 'actions', label: ''},
            ],
            activePage: 1,
            perPage: 1,
			currentPage: 1,
            filter: {
                level: null
            },
        }
    },
    computed: {
        ...mapState(['characteristics', 'positive_sides', 'negative_sides', 'users']),
        rows() {
			return this.characteristics.list.length;
		},
		lists() {
			const items = this.characteristics.list;
			return items.slice(
				(this.currentPage - 1) * this.perPage,
				this.currentPage * this.perPage
			);
		},
    },
    methods: {
        ...mapActions({
                saveCharacteristics: 'characteristics/saveItem',
                deleteCharacteristics: 'characteristics/deleteItem',
                getCharacteristics: 'characteristics/getList',
                getPositiveSides: 'positive_sides/getList',
                getNegaiveSides: 'negative_sides/getList',
            })
    },
    async created() {
        this.$store.state.breadcrumbs = [
            {text: 'Главная', to: {name: 'home'}},
            { text: "Характеристики", to: { name: "characteristics" } },
        ];

        await this.getNegaiveSides().then(list => {
            console.log(list)
        })
        .catch(error => {
            console.log(error)
        });
        
        await this.getPositiveSides().then(list => {
            console.log(list)
        })
        .catch(error => {
            console.log(error)
        });
        
        await this.getCharacteristics().then(list => {
            console.log(list)
        })
        .catch(error => {
            console.log(error)
        });

        await this.$store
			.dispatch("users/getList")
			.then((item) => {
				console.log(item);
			})
			.catch((error) => {
				console.log(error);
			});
    }
}
</script>

<style scoped>

</style>
