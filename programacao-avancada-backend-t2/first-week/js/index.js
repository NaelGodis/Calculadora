//Overview de JavaScript

// coonsole
console.log('texto')
console.error('Algo errado não está certo!')
console.warn('Fica Esperto.')

//variavies
const nome = "victor"
console.log(nome)
let x =10
if(true)
{
    let x = 10
}

console.log(x)

//tipos de dados

//string
const name = "victor"
console.log(nome)
console.log(typeof nome)
n = 15,99
console.log(n)
console.log(typeof n)

//bol
const isOpen = 0
console.log(isOpen)
console.log(typeof isOpen)

//null
const a = null
console.log(a)
console.log(typeof a)

//undefined
let nada 
console.log(nada)
console.log(typeof nada)

//array
const linguagens = ["c++",50,"java","python","JS"]
console.log(linguagens[1])
console.log(typeof linguagens[1])


//object literals
const user = {
    username: "Nael", 
    password: "123",
    age: 31,
    name: "Nael Godis"
}
console.log(user)
console.log(typeof user)

//métodos de string
 const text = 'Qualquer um'
 console.log(text.length)
 //quebrar texto em conjunto de caracteres
const textToArray = text.split("quer")
console.log(textToArray[1])

// tornar as letras maiusculas
console.log(text.toLocaleUpperCase())

//procurar algo dentreo da string
console.log(text.indexOf("m"))
console.log(text.charAt(text.length -1))
console.log(text.slice(4,11))

//mais sobre arrays
const chars =['AAA','B','C','D',88]
console.log(chars.length -1)
console.log(chars[chars.length -1])
chars[5] = "F"
console.log(chars)
chars.pop()
chars.unshift("B")
console.log(chars)

