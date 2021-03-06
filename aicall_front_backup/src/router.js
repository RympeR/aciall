import Vue from 'vue'
import Router from 'vue-router'

import TheContainer from './containers/TheContainer.vue';
import Login from './components/Login.vue';
import ChangePassword from "./views/ChangePassword";
import Home from "./views/Home";

import StudentList from "./views/user/student/StudentList";
import StudentForm from "./views/user/student/StudentForm";


import CountryList from "@/views/info/country/CountryList"
import CountryForm from "@/views/info/country/CountryForm"


import EducationList from "@/views/info/education/EducationList"
import EducationForm from "@/views/info/education/EducationForm"

import PositiveSidesList from "@/views/info/positive_sides/PositiveSidesList"
import PositiveSidesForm from "@/views/info/positive_sides/PositiveSidesForm"

import NegativeSidesList from "@/views/info/negative_sides/NegativeSidesList"
import NegativeSidesForm from "@/views/info/negative_sides/NegativeSidesForm"

import LanguageList from "@/views/info/language/LanguageList"
import LanguageForm from "@/views/info/language/LanguageForm"

import ShortcodeList from "@/views/user/shortcode/ShortcodeList"
import ShortcodeForm from "@/views/user/shortcode/ShortcodeForm"

import CharacteristicsList from "@/views/user/characteristics/CharacteristicsList"
import CharacteristicsForm from "@/views/user/characteristics/CharacteristicsForm"


import ActionAreaList from "@/views/info/actionarea/ActionAreaList"
import ActionAreaForm from "@/views/info/actionarea/ActionAreaForm"

import TalkThemeList from "@/views/info/talktheme/TalkThemeList"
import TalkThemeForm from "@/views/info/talktheme/TalkThemeForm"


Vue.use(Router);

export default new Router({
	mode: 'history',
	// mode: 'hash',
	linkActiveClass: 'active',
	base: process.env.BASE_URL,
	routes: [
		{
			path: '/login',
			name: 'login',
			component: Login,
			meta: {
				requiresAuth: false
			},
		},
		{
			path: '/',
			name: 'main',
			component: TheContainer,
			redirect: 'home',
			meta: {
				requiresAuth: true
			},
			children: [
				{
					path: 'home',
					name: 'home',
					component: Home,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'change-password',
					name: 'change-password',
					component: ChangePassword,
					meta: {
						requiresAuth: true
					},
				},

				{
					path: 'user/student',
					name: 'students',
					component: StudentList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'user/student/update/:id',
					name: 'student-update',
					component: StudentForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'user/student/create',
					name: 'student-create',
					component: StudentForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'info/country/create',
					name: 'country-create',
					component: CountryForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'info/country',
					name: 'countries',
					component: CountryList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'info/country/update/:id',
					name: 'country-update',
					component: CountryForm,
					meta: {
						requiresAuth: true
					}
				},

				{
					path: 'info/education/create',
					name: 'education-create',
					component: EducationForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'info/education',
					name: 'educations',
					component: EducationList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'info/education/update/:id',
					name: 'education-update',
					component: EducationForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'info/language/create',
					name: 'language-create',
					component: LanguageForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'info/language',
					name: 'languages',
					component: LanguageList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'info/language/update/:id',
					name: 'language-update',
					component: LanguageForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'user/shortcode/create',
					name: 'shortcode-create',
					component: ShortcodeForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'user/shortcode',
					name: 'shortcodes',
					component: ShortcodeList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'user/shortcode/update/:id',
					name: 'shortcode-update',
					component: ShortcodeForm,
					meta: {
						requiresAuth: true
					}
				},

				{
					path: 'info/actionarea/create',
					name: 'actionarea-create',
					component: ActionAreaForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'info/actionarea',
					name: 'actionareas',
					component: ActionAreaList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'info/actionarea/update/:id',
					name: 'actionarea-update',
					component: ActionAreaForm,
					meta: {
						requiresAuth: true
					}
				},

				{
					path: 'info/talktheme/create',
					name: 'talktheme-create',
					component: TalkThemeForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'info/talktheme',
					name: 'talkthemes',
					component: TalkThemeList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'info/talktheme/update/:id',
					name: 'talktheme-update',
					component: TalkThemeForm,
					meta: {
						requiresAuth: true
					}
				},

				{
					path: 'info/positive-side/create',
					name: 'positive-sides-create',
					component: PositiveSidesForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'info/positive-side',
					name: 'positive-sides',
					component: PositiveSidesList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'info/positive-side/update/:id',
					name: 'positive-sides-update',
					component: PositiveSidesForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'info/negative-side/create',
					name: 'negative-sides-create',
					component: NegativeSidesForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'info/negative-side',
					name: 'negative-sides',
					component: NegativeSidesList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'info/negative-side/update/:id',
					name: 'negative-sides-update',
					component: NegativeSidesForm,
					meta: {
						requiresAuth: true
					}
				},
				{
					path: 'info/characteristics',
					name: 'characteristics',
					component: CharacteristicsList,
					meta: {
						requiresAuth: true
					},
				},
				{
					path: 'info/characteristics/update/:id',
					name: 'characteristics-update',
					component: CharacteristicsForm,
					meta: {
						requiresAuth: true
					}
				},

				
				

			]
		},
	],
})
