from PyInquirer import style_from_dict, Token, prompt, Separator

style = style_from_dict({
    Token.Separator: '#E91E63',
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

questions_initial = [
    {
        'type': 'input',
        'name': 'restaurantName',
        'message': "What's the restaurant name?"
    },
    {
        'type': 'input',
        'name': 'latitude',
        'message': "Type a latitude near the restaurant:",
        'filter': lambda a: float(a)
    },
    {
        'type': 'input',
        'name': 'longitude',
        'message': "Type a longitude near the restaurant:",
        'filter': lambda a: float(a)
    }
]

questions_restaurant = [
    {
        'type': 'list',
        'message': 'Select your restaurant',
        'name': 'restaurantSelector',
        'choices': [
            Separator('= Restaurants =')
        ]
    }
]

questions_image = [
    {
        'type': 'confirm',
        'message': 'Do you want to download the images?',
        'name': 'downloadImages',
        'default': True,
    }
]