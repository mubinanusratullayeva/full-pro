const lable = document.querySelector('.navbar__menu-switch')
const spanPlayer = document.querySelector('.navbar__menu-switchBtn')
const navbar = document.querySelector('.navBoss')
const HeroHead = document.querySelector('.heroTop')
const popDiv = document.querySelector('.bgFf')
const regDiv = document.querySelector('.bgFe')
const abu = document.querySelector('.abu')
const cardsItem = document.querySelectorAll('.cards__item')
const updates = document.querySelector('.updates')
const cardShish = document.querySelectorAll('.menuPack__dishCards-item')
const titleH = document.querySelectorAll('h3, h4, h5, h6')
const allButtons = document.querySelectorAll('button')
const testimony = document.querySelector('.testimony')
const testimonyCards = document.querySelectorAll('.flexBoxKrop__cards-item')

let themeMode = localStorage.getItem("theme");

if (themeMode !== 'dark') {
    HeroHead.classList.remove('CheangedHero')
    spanPlayer.classList.remove('changePos')
    popDiv.classList.remove('darkPop')
    navbar.classList.remove('darknav')
    abu.classList.remove('darkabu')
    updates.classList.remove('darkupdates')
    cardsArrayRe(cardsItem, cardShish, titleH, allButtons, testimonyCards)
    regDiv.classList.remove('regDiv')
    testimony.classList.remove('testimonyAg')
} else {
    updates.classList.add('darkupdates')
    navbar.classList.add('darknav')
    abu.classList.add('darkabu')
    HeroHead.classList.add('CheangedHero')
    regDiv.classList.add('regDiv')
    spanPlayer.classList.add('changePos')
    popDiv.classList.add('darkPop')
    testimony.classList.add('testimonyAg')
    cardsArray(cardsItem, cardShish, titleH, allButtons, testimonyCards)
}

function cardsArray(param1, param2, param3, param4, param5) {
    param1.forEach(item => {
        item.classList.add('cardsItem')
    })

    param2.forEach(item => {
        item.classList.add('darkCardShish')
    })

    param3.forEach(item => {
        item.classList.add('darkTitle')
    })

    param4.forEach(item => {
        item.classList.add("btnFontColor")
    })

    param5.forEach(item => {
        item.classList.add('testimonyCard')
    })
}
//functions for cards
function cardsArrayRe(param1, param2, param3, param4, param5) {
    param1.forEach(item => {
        item.classList.remove('cardsItem')
    })

    param2.forEach(item => {
        item.classList.remove('darkCardShish')
    })

    param3.forEach(item => {
        item.classList.remove('darkTitle')
    })

    param4.forEach(item => {
        item.classList.remove("btnFontColor")
    })

    param5.forEach(item => {
        item.classList.remove('testimonyCard')
    })
}

lable.addEventListener('click', () => {
    if (themeMode === 'dark') {
        popDiv.classList.remove('darkPop')
        regDiv.classList.remove('regDiv')
        HeroHead.classList.remove('CheangedHero')
        spanPlayer.classList.remove('changePos')
        navbar.classList.remove('darknav')
        abu.classList.remove('darkabu')
        updates.classList.remove('darkupdates')
        localStorage.setItem('theme', 'light')
        testimony.classList.remove('testimonyAg')
        cardsArrayRe(cardsItem, cardShish, titleH, allButtons, testimonyCards)
    } else {
        updates.classList.add('darkupdates')
        abu.classList.add('darkabu')
        popDiv.classList.add('darkPop')
        navbar.classList.add('darknav')
        regDiv.classList.add('regDiv')
        HeroHead.classList.add('CheangedHero')
        spanPlayer.classList.add('changePos')
        testimony.classList.add('testimonyAg')
        localStorage.setItem('theme', 'dark')
        cardsArray(cardsItem, cardShish, titleH, allButtons, testimonyCards);
    }
})
