const pokemon_id = document.querySelector('.pokemon_id');
const id = document.querySelector('#input');

const getPokemon = function (value) {
   fetch(`https://pokeapi.co/api/v2/pokemon/${value}`)
      .then((response) => response.json())
      .then((data) => showData(data));
};

function showData(data) {
   const pokeName = data.name[0].toUpperCase() + data.name.substring(1);
   const pokeHeight = data.height;
   const pokeWeight = data.weight;
   const pokeType = data.types;
   const pokeImg = data.sprites.front_default;

   const image = document.querySelector('.img');
   const name = document.querySelector('.name');
   const height = document.querySelector('.height');
   const weight = document.querySelector('.weight');
   const type = document.querySelector('.type');

   name.textContent = pokeName;
   image.src = pokeImg;
   height.textContent = `Altura: ${pokeHeight / 10} m`;
   weight.textContent = `Peso: ${pokeWeight / 10} kg`;
   type.innerHTML = '<h4>Tipo:</h4>';
   pokeType.forEach((element) => {
      let typeElement =
         element.type.name[0].toUpperCase() + element.type.name.substring(1);
      let ul = document.createElement('ul');
      let list = type.appendChild(ul);
      let li = document.createElement('li');
      li.textContent = `${typeElement}`;
      list.appendChild(li);
   });
}

// getPokemon:
function getPokemonId() {
   const value = id.value;
   let pokemonData = getPokemon(value);
   savePokemon();
}

const btn = document.querySelector('.btn');
btn.addEventListener('click', getPokemonId);