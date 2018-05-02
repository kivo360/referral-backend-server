let url = "https://refer.funguana.com";
let data = {
    email: localStorage.getItem('email', ''),
    responseMsg: '',
    viewResponse: false,
    successful: false,
    showEmail: true,
    referralCode: localStorage.getItem('referral', ''),
    referral_url: 'https://funguana.com/?ref=' + localStorage.getItem('referral', '')
}

function initialize(){
    if(data.referralCode === null){
        $("#referralContainer").hide();
        $("#responseContainer").hide();
    }else{
        $("#emailContainer").hide();
    }
}

function updateDom(){
    if (data.responseMsg !== '') {
        // Check to see if we should show the success
        
        if(data.viewResponse === true){
            console.log(data.responseMsg);
            $("#responseContainer").show();
            
            $("#responseMsg").show().text(data.responseMsg);

            if (localStorage.getItem('referral', '') !== null){
                console.log(data.referral_url);
                $("#referralContainer").show();
                $("#referralUrl").show().text(data.referral_url);
                $("#referralUrl").click(function () {
                    new ClipboardJS('#referralUrl', {
                        text: function () {
                            return data.referral_url;
                        }
                    });
                });
            }else{
                $("#referralContainer").hide();
            }
            
        }
        if (data.successful) {
            $("#emailContainer").hide();
        }
    }
    if(data.referralCode !== null){
        $("#emailContainer").hide();
        $("#responseContainer").show();
        $("#referralContainer").show();
        // $("#responseMsg").show().text(data.responseMsg);
        $("#referralUrl").show().text(data.referral_url);
        $("#referralUrl").click(function () {
            new ClipboardJS('#referralUrl', {
                text: function () {
                    return data.referral_url;
                }
            });
        });
    }
}
setTimeout(function(){
    initialize();
    updateDom();
}, 500);

function buttonClick(){
    console.log("Button was clicked");
    const self = this;
    var config = {
        headers: {
            'Access-Control-Allow-Origin': '*'
        }
    };
    console.log("Button was clicked")
    // app.submitEmail();
    if (data.email === '') {
        data.responseMsg = "Please Enter Something";
        data.viewResponse = true;
        
        // $('#errors').show();
        return;
    }

    new Promise(function(resolve, reject){
        resolve("variable");
    }).then(result => axios.get("https://api.ipdata.co"))
    .then(result=>result.data.ip)
    .then(ip_address=>{
        
        var user_data = {
            user_ip: ip_address,
            email: data.email
        };
        var ref = getParameterByName('ref');
        if (ref !== null || ref !== null) {
            user_data.referer = ref;
        }
        return user_data;
    })
    .then(user_data => axios.post(url + '/register', user_data, config))
    .then(response=>{
        // console.log(response)
        data.successful = response.data.success;
        data.responseMsg = response.data.msg;
        data.viewResponse = true;


        if (data.successful === true) {
            localStorage.setItem('email', data.email);
        }

        if (response.data.referral_code !== null && response.data.referral_code !== undefined) {
            data.referralCode = response.data.referral_code;
            data.referralCode = 'https://funguana.com/?ref=' + response.data.referral_code;
            data.referral_url = 'https://funguana.com/?ref=' + response.data.referral_code;
            data.showEmail = false;

            localStorage.setItem('referral', response.data.referral_code)
        }
        return true;
    })
    .then(value=>updateDom())
    .catch(ip_error=>{
        console.log(ip_error);
    });


    // axios.get("https://api.ipdata.co").then(function (ip_results) {
    //     var laemail = data.email;
    //     // user_ip = request.json.get('user_ip', None)
    //     // email = request.json.get('email', None)
    //     // referred_by = request.json.get('referer',None) 
    //     var user_data = {
    //         user_ip: ip_results.data.ip,
    //         email: laemail
    //     };
    //     // console.log(user_data);
    //     var ref = getParameterByName('ref');
    //     console.log(ref);
    //     if (ref !== null || ref !== null) {
    //         user_data.referer = ref;
    //     }
    //     // console.log(ip_results)
    //     axios.post(url + '/register', user_data, config).then(function (response) {
    //         data.successful = response.data.success;
    //         data.responseMsg = response.data.msg;
    //         data.viewResponse = true;
        

    //         if (data.successful === true) {
    //             localStorage.setItem('email', laemail);
    //         }

    //         if (response.data.referral_code !== null && response.data.referral_code !== undefined) {
    //             data.referralCode = response.data.referral_code;
    //             data.referralCode = 'https://funguana.com/?ref=' + response.data.referral_code;
    //             data.referral_url = 'https://funguana.com/?ref=' + response.data.referral_code;
    //             data.showEmail = false;
                
    //             localStorage.setItem('referral', response.data.referral_code)
    //         }
    //     }).catch(function (error) {
    //         console.log(error);
    //     });
    // }).catch(function (ip_error) {
    //     console.log(ip_error);
    // });

}

function activateHandlers(){
    $("#emailSubmitButton").click(function(){
        buttonClick();
    })
    $(window).keyup(function () {
        data.email = $('#enterEmail').val();
        // console.log(data.email);
    });
    
}





activateHandlers();
