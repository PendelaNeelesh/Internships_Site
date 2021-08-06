import jQuery from 'jquery'

const state = {
		forminfo: {
			comp: " ",
			email: " ",
			title: " ",
			type: " ",
			loc: " ",
			pay: 0,
			desc: " ",
			id: 0,
		}

	}

const getters = {
	
	getformdata: (state)=>{
		return state.forminfo;
	},

}



const actions = {
	modifyintern : async function (state,data){
		await jQuery.ajax({
			url: `/users/mod`,
			type: 'POST',
			data: data,
			success: function(data,status,xhr){
				if(data.message=="Updated"){
					window.alert("Updated")
					state.state.forminfo.comp = " "
					state.state.forminfo.email = " "
					state.state.forminfo.loc = " "
					state.state.forminfo.title = " "
					state.state.forminfo.pay = 0
					state.state.forminfo.desc = " "
					state.state.forminfo.type = " "
				}
			}
		
		})
	},
}


const mutations = {


}


export default{
	state,
	getters,
	actions,
	mutations

};
