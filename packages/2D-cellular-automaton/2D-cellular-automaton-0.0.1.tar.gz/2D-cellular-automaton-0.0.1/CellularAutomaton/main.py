from .automaton import Automaton


def main():
    rows = 1000
    rule = 57
    block_size = 1
    starting_indicies = []
    path = f'{starting_indicies}.jpeg'

    automaton = Automaton(rows=rows, starting_indicies=starting_indicies,
                          rule=rule, method='New')

    image = automaton.image(block_size=block_size)
    image.save(path, format='jpeg')


if __name__ == '__main__':
    main()
