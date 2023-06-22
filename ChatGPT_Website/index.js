function submitForm(e) {
    e.preventDefault();
    getData();

}

async function getData() {
    let userData = document.getElementById("input").value.trim();
    if(userData == "") return false;

    document.getElementById("messages").innerHTML = `<div class="mess-user">
        <p>${userData}</p>
    </div>` + document.getAnimations("messages").innerHTML
    document.getElementById("input").value = ""


    const API =  'your openai KEY';
    


    try {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${API}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: 'gpt-3.5-turbo',
                messages: [{role: 'user', content: userData}],
                max_tokens: 100
                
            })
        })

        const data = await response.json()
        //console.log(data) 
        //from console.log(data) we get idea where the messages are shown and then the code 
        //data.choices[0].message.content to show the messages in the browser 

        document.getElementById("messages").innerHTML = `<div class="mess-chat">
            <p>${data.choices[0].message.content}</p>
        </div>` + document.getElementById("messages").innerHTML
    } catch (error) {
        console.error('Eror: ', error)
        
    }
}
