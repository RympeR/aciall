// import axios from '@/plugins/axios'
import axios from 'axios'

const state = () => ({
    list: [],
    item: {},
})

const mutations = {
    setList(state, list) {
        state.list = list;
    },
    setItem(state, item) {
        state.item = item;
    },

}

const actions = {
    getList({commit}) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_HOST+'/api/user/get-characteristics-list', {
                    // params: this.linesSearch,
                    headers: {
                        Authorization: "tset",
                    }
                })
                .then(response => {
                    let list = response.data.results;
                    console.log(list)
                    list.forEach((el) => {
                        el.first_user_phone = el.sender.phone
                        el.first_user_name = el.sender.username
                        el.sec_user_phone = el.reciever.phone
                        el.sec_user_name = el.reciever.username
                        el.positive_side = []
                        el.negative_side = []
                        el.positive_sides.forEach((elem)=>{
                            el.positive_side.push(elem.name_ru)
                        } )
                        el.positive_side = el.positive_side.join(', ')
                        el.negative_sides.forEach((elem)=>{
                            el.negative_side.push(elem.name_ru)
                        } )
                        el.negative_side = el.negative_side.join(', ')
                    });
                    
                    commit('setList', list);

                    resolve(list);

                })
                .catch(response => {
                    reject(response.error);
                })
        })
    },
    getItem({commit}, id) {
        return new Promise((resolve, reject) => {
            axios.get(process.env.VUE_APP_HOST + `/api/user/get-characteristics/${id}`, {
                    // params: this.linesSearch,
                    headers: {
                        Authorization: "tset",
                    }
                })
                .then(response => {
                    let item = response.data;
                    item.positive_side = []
                    item.negative_side = []
                    item.positive_sides.forEach((elem)=>{
                        item.positive_side.push(elem.name_ru)
                    } )
                    item.positive_side = item.positive_side.join(', ')
                    item.negative_sides.forEach((elem)=>{
                        item.negative_side.push(elem.name_ru)
                    } )
                    item.negative_side = item.negative_side.join(', ')
                    commit('setItem', item);
                    resolve(item)
                })
                .catch(response => {
                    reject(response.error);
                })
        })
    }, 
    deleteItem({state}, id) {
        let confirmDelete = confirm('Вы действительно хотите удалить эту характеристику?');
        if (confirmDelete) {
            return new Promise((resolve, reject) => {
                axios.delete(`${process.env.VUE_APP_HOST}/api/user/delete-characteristics/${id}`,
                {
                    headers: {
                      Authorization: "tset",
                    },
                  }
                )
                    .then(response => {
                        state.list = state.list.filter(element => element.id !== id);
                        resolve(response.data);
                    })
                    .catch(response => {
                        console.log(response.error);
                        reject(response.error);
                    })
            })
        }
    },
    getFilteredItems({commit, state}, obj){
        console.log(obj)
        console.log(state)
        var str = `${process.env.VUE_APP_HOST}/api/user/get-characteristics-list?`;
        for (var key in obj) {
            if (str != `${process.env.VUE_APP_HOST}/api/user/get-characteristics-list?`) {
                str += "&";
            }
            str += key + "=" + encodeURIComponent(obj[key]);
        }
        console.log(str)
        return new Promise((resolve, reject) =>{
            axios
            .get(str)
            .then(response => {
                let list = response.data.results;
                list.forEach((el) => {
                    el.first_user_phone = el.sender.phone
                    el.first_user_name = el.user.username
                    el.sec_user_phone = el.reciever.phone
                    el.sec_user_name = el.reciever.username
                    el.positive_side = []
                    el.negative_side = []
                    el.positive_sides.forEach((elem)=>{
                        el.positive_side.push(elem.name_ru)
                    } )
                    el.positive_side = el.positive_side.join(', ')
                    el.negative_sides.forEach((elem)=>{
                        el.negative_side.push(elem.name_ru)
                    } )
                    el.negative_side = el.negative_side.join(', ')
                });
                console.log(list)
                commit('setList', list);
                resolve(list);
            })
            .catch(response => {
                reject(response.error);
            })
        })
    },
    saveItem({state}, obj) {
        console.log(state)
        console.log(obj.id)
        obj.user = obj.user.id;
        obj.line = obj.line.id;
        obj.container = obj.container.id;
        obj.city = obj.city.id;
        let formData = new FormData();
        
        Object.keys(obj).map(function (key) {
            if (obj[key])
                formData.append(key, obj[key]);
        });
        
        if (obj.id) {
            return new Promise((resolve, reject) => {
                axios
                    .put(process.env.VUE_APP_HOST + '/api/user/update-characteristics/' + obj.id, formData, {
                            headers: {
                                Authorization: "tset",
                                // 'Content-Type': 'multipart/form-data'
                            },
                        }
                    )
                    .then(response => {
                        console.log(this)
                        state.item = {};
                        resolve(response.data);
                    })
                    .catch(response => {
                        console.log(response.error);
                        reject(response.error);
                    })
            })
        } else {
            return new Promise((resolve, reject) => {
                axios.post(process.env.VUE_APP_HOST + '/api/info/create-characteristics/', formData, {
                        headers: {
                            Authorization: "tset",
                            'Content-Type': 'multipart/form-data',
                        },
                    })
                    .then(response => {
                        state.item = {};
                        resolve(response.data)
                        // console.log(response.data)
                    })
                    .catch(response => {
                        reject(response.error);
                    })
            })
        }
    },
}

const getters = {

}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}