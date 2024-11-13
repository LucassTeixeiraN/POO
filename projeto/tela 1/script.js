// pra abrir a aba de filtro

const filtroContainer = document.getElementById("filtro-container")
const inputContainer = document.getElementById("input-container")
const gamesSelectedContainer = document.getElementById("games-selected")
let openned = false
let gameArr = [] 

function openFiltro() {
    if(openned === false) {
        filtroContainer.setAttribute("class", "modal-activated")
        inputContainer.setAttribute("class", "activated")
        gamesSelectedContainer.setAttribute("class", "activated")
        openned = true
    } else {
        filtroContainer.setAttribute("class", "modal-disabled")
        inputContainer.setAttribute("class", "disabled")
        gamesSelectedContainer.setAttribute("class", "disabled")
        openned = false
    }

}

//Selecionando jogos
function addGame() {
    let gameSelection = document.getElementById("games-options")
    let game = gameSelection.options[gameSelection.selectedIndex].text

    if (game !== "Selecione um jogo" && findGame(game) === true){
        // Cria os elementos
        let gameContainer = document.createElement("div")
        let gameName = document.createElement("p")
        let deleteBtn = document.createElement("button")

        // Da append deles num elemento pai
        gamesSelectedContainer.appendChild(gameContainer)
        gameContainer.appendChild(gameName)
        gameContainer.appendChild(deleteBtn)

        //Coloca texto dentro deles
        gameName.innerHTML = game
        deleteBtn.innerHTML = "X"

        //Setta os atributos
        gameContainer.setAttribute("id", "game-container")
        deleteBtn.setAttribute("onclick", "deleteGame()")

        //Adiciona o jogo no array
        gameArr.push(game)
    }
}

// Garante que um jogo que já foi adicionado seja adicionado novamente
function findGame(game){
    for(var i = 0; i < gameArr.length; i++) {
        if(gameArr[i] === game) {
            return false
        }
    }
    return true
}

