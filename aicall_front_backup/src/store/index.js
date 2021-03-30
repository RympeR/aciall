import Vue from 'vue'
import Vuex from 'vuex'
import axios from '@/plugins/axios'

import users from './modules/users'

import admin from './modules/admin'

import country from './modules/country'
import actionarea from './modules/actionarea'
import talktheme from './modules/talktheme'
import shortcode from './modules/shortcode'
import language from './modules/language'
import education from './modules/education'

import positive_sides from './modules/positive_sides'
import negative_sides from './modules/negative_sides'
import characteristics from './modules/characteristics'

Vue.use(Vuex);

export default new Vuex.Store({
    // namespaced: true,
    state: {
        status: '',
        token: localStorage.getItem('token') || null,
        profile: null,
        breadcrumbs: [
            {text: 'Главная', to: {name: 'home'}},
        ],
        password: localStorage.getItem('password') || null,
    },

    mutations: {
        auth_request(state) {
            state.status = 'loading'
        },
        auth_success(state, token) {
            state.status = 'success';
            state.token = token
        },
        auth_error(state) {
            state.status = 'error'
        },
        logout(state) {
            state.status = '';
            state.token = ''
        },
    },
    actions: {
        login({commit}, user){
            console.log(user)
            return new Promise((resolve, reject) => {
                commit('auth_request');
                let formData = new FormData();
                Object.keys(user).map(function (key) {
                    if (user[key])
                        formData.append(key, user[key]);
                });
                console.log(this)
                axios.post(process.env.VUE_APP_HOST + '/auth/token/login/', formData)
                .then(response => {
                    console.log(response);
                    const token = response.data.auth_token;
                    localStorage.setItem('token', token);
                    localStorage.setItem('password', user.password);
                    // Vue.prototype.$axios.defaults.common['token'] = token;
                    axios.defaults.headers.common['Authorization'] = token;
                    console.log(axios)
                    commit('auth_success', token);
                    resolve(response)
                })
                .catch(response => {
                    console.log(response);
                    commit('auth_error');
                    localStorage.removeItem('token');
                    reject(response)
                })
            })
        },
        logout({commit}){
            return new Promise((resolve, reject) => {
                commit('logout');
                localStorage.removeItem('token');
                // Vue.prototype.$axios.defaults.headers.common['token'] = '';
                delete axios.defaults.headers.common['Authorization'];
                // delete axios.defaults.headers.common['Authorization']
                resolve();
                console.log(reject)
            })
        },
        token(){
            return new Promise((resolve) => {
                resolve('Token ' + this.state.token)
            })
        }
    },
    getters: {
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status,
    },
    modules: {
        users,
        admin,
        country,
        actionarea,
        talktheme,
        shortcode,
        language,
        education,
        positive_sides,
        negative_sides,
        characteristics,
    }
})