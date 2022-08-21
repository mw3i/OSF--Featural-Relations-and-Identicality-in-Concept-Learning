var instructions = {

    start: function(params, next) {

        // INSTRUCTIONS (see materials/styles.css for styling info)
        instructions_div = document.createElement('div')
        instructions_div.id = 'instructions_div'
        document.getElementById('main').appendChild(instructions_div)

        instructions_text = document.createElement('p')
        instructions_text.innerHTML = params["instructions"]

        instructions_text.id = 'instructions_text'
        document.getElementById('instructions_div').appendChild(instructions_text)


        // Continue Button
        start_button = document.createElement('button')
        start_button.innerHTML = "Next"

        start_button.id = 'start_button'
        start_button.style = 'font-size: 50px; padding: 5px'
        document.getElementById('instructions_div').appendChild(start_button)
        start_button.addEventListener("click", function () {
            document.getElementById('main').innerHTML = ''
            next()
        })

        console.log('started instructions')
    },

}
