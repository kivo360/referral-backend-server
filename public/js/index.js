let url = "http://localhost:8000";
let data = {
    email: localStorage.getItem('email', ''),
    errorMessage: '',
    viewSuccess: false,
    successful: false,
    referralCode: localStorage.getItem('referral', '')
}



var app = new Vue({
    el: '#referral_fields',
    data: data,
    methods: {
        submitEmail: function(){
            const self = this;
            axios.get("https://api.ipdata.co").then(function (ip_results) {

                var laemail = self.email;
                if (laemail === '') {
                    $('#errors').text("Please Enter Something");
                    $('#errors').show();
                    return;
                }
                // user_ip = request.json.get('user_ip', None)
                // email = request.json.get('email', None)
                // referred_by = request.json.get('referer',None) 
                var user_data = {
                    user_ip: ip_results.data.ip,
                    email: laemail
                };
                // console.log(user_data);
                var ref = getParameterByName('ref');
                if (ref !== null || ref !== null) {
                    user_data.referer = ref;
                }

                axios.post(url + '/register', user_data).then(function (response) {
                    self.successful = response.data.success;
                    self.errorMessage = response.data.msg;
                    self.viewSuccess = true;
                    if (self.successful === true){
                        localStorage.setItem('email', laemail);
                    }

                    if (response.data.referral_code !== null){
                        self.referralCode = response.data.referral_code;
                        localStorage.setItem('referral', response.data.referral_code)
                    }
                    console.log(response.data);
                }).catch(function (error) {
                    console.log(error);
                });
                // console.log(user_data);
                // registerUser(user_data);
            }).catch(function (ip_error) {
                console.log(ip_error);
            });
        }
    }
})

// console.log(data);
if (data.referralCode !== '') {
    data.viewSuccess = true;
    app.$forceUpdate();
}
// function start() {
    
// }
// start();