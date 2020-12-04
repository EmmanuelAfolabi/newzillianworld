var updateBtns = document.getElementsByClassName('aquarium-update-bag')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)
        console.log('USER:', user)

        if (user == 'AnonymousUser'){
            addCookieItem(productId, action)

        }else{
            updateUserOrder(productId, action)
        }
    })
}

function addCookieItem(productId, action){
    console.log("Please log in")

    if (action == 'add'){
        if (bag[productId] == undefined){
            bag[productId] = {'quantity':1}
        }else{
            bag[productId]['quantity'] += 1
        }
    }

    if (action == 'remove'){
        bag[productId]['quantity'] -= 1

        if (bag[productId]['quantity'] <= 0){
            console.log('Item should be deleted')
            delete bag[productId]
        }
    }
    console.log('bag:', bag)
    document.cookie = 'bag=' + JSON.stringify(bag) + ";domain=;path=/"
    location.reload()
}


function updateUserOrder(productId, action){
        var url = '/update_item'
        console.log('URL:', url)
        fetch(url,{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'productId':productId, 'action':action})
        })
        .then((response) =>{
            return response.json();
        })
        .then ((data) =>{
            console.log('data:', data)
            location.reload()
        });
}

