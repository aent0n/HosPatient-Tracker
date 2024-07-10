document.getElementById('inscription').addEventListener('submit', function(event) {
    event.preventDefault(); 

    
    const nom = document.getElementById('nom').value;
    const prenom = document.getElementById('prenom').value;
    const numTel = document.getElementById('numTel').value;
    const mail = document.getElementById('mail').value;
    const password = document.getElementById('password').value;
    const passwordConf = document.getElementById('passwordConf').value;

    
    const data = { nom: nom, prenom: prenom, numTel: numTel, mail: mail, password, password, passwordConf, passwordConf};

    
    if (!(password === passwordConf)){
        document.getElementById('errortext').innerHTML= "Echec de la confirmation du mot de passe"
    }else{

        
        fetch('/inscription', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' 
            },
            body: JSON.stringify(data) 
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json(); 
        })
        .then(data => {
            console.log('Success:', data); 
            //document.getElementById('response').innerText = JSON.stringify(data, null, 2);
        })
        .catch((error) => {
            console.error('Error:', error); 
            document.getElementById('errortext').innerText = 'Error: ' + error.message; 
        });
    }
});
