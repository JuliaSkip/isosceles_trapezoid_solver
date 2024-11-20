import re
from trapezoid import Solver
from udpipe_analyse import TaskExtractor, TextPreprocessor, UDPipeAPI


class GeometryTaskAnalyser:
    taxonomy = {
        'bases': ['більша основа', 'менша основа', 'сума основ'],
        'sides': ['бічна сторона'],
        'height': ['висота'],
        'perimeter': ['периметр'],
        'area': ['площа'],
        'angles': ['кут', 'сума кутів', 'різниця кутів'],
        'middle line': ['середня лінія'],
        'diagonal': ['діагональ']
    }

    @staticmethod
    def get_task_data(significant_words):
        task_data = {
            'bigger base': None,
            'circle': None,
            'bigger base small': None,
            'bigger base large': None,
            'smaller base': None,
            'sum bases': None,
            'side': None,
            'height': None,
            'height present': None,
            'perimeter': None,
            'area': None,
            'angle': None,
            'sum angles': None,
            'diff angles': None,
            'middle line': None,
            'diagonal': None
        }

        english_letter_regex = re.compile(r'[a-z]')
        for i, word in enumerate(significant_words):
            if word == 'коло':
                task_data['circle'] = 1
            if word == 'висота':
                task_data['height present'] = 1
            if word.isdigit() or english_letter_regex.match(word):

                if i > 0 and "більший" in significant_words[i - 2] and "менший" in significant_words[i - 3]:
                    task_data['bigger base'] = significant_words[i + 2]
                    task_data['smaller base'] = word

                elif i > 0 and "менший" in significant_words[i - 2] and "більший" in significant_words[i - 3]:
                    task_data['bigger base'] = word
                    task_data['smaller base'] = significant_words[i + 2]

                elif i > 0 and "середній" in significant_words[i - 2]:
                    task_data['middle line'] = word

                elif i > 0 and "більший" in significant_words[i - 2]:
                        task_data['bigger base'] = word

                elif i > 0 and "менший" in significant_words[i - 2]:
                    task_data['smaller base'] = word

                elif i > 0 and "основа" in significant_words[i - 1] and significant_words[i + 2].isdigit():
                    task_data['bigger base'] = significant_words[i + 2] if word < significant_words[i + 2] else word
                    task_data['smaller base'] = significant_words[i + 2] if word > significant_words[i + 2] else word

                elif i > 0 and "висота" in significant_words[i - 1]:
                    task_data['height'] = word

                elif i > 0 and "бічний" in significant_words[i - 2]:
                    task_data['side'] = word

                elif i > 0 and "ділити" in significant_words[i - 4] and "більший" in significant_words[i - 3]:
                    task_data['bigger base small'] = significant_words[i + 2] if word < significant_words[i + 2] else word
                    task_data['bigger base large'] = significant_words[i + 2] if word > significant_words[i + 2] else word
                    task_data['bigger base'] = float(word) + float(significant_words[i + 2])
                    task_data['smaller base'] = abs(float(word) - float(significant_words[i + 2]))

                elif i > 0 and "периметр" in significant_words[i - 1]:
                    task_data['perimeter'] = word

                elif i > 0 and "сума" in significant_words[i - 2] and "основа" in significant_words[i - 1]:
                    task_data['sum bases'] = word

                elif i > 0 and "площа" in significant_words[i - 1]:
                    task_data['area'] = word

                elif i > 0 and "сума" in significant_words[i - 3] and "кут" in significant_words[i - 1]:
                    task_data['sum angles'] = word

                elif i > 0 and "різниця" in significant_words[i - 3] and "кут" in significant_words[i - 1]:
                    task_data['diff angles'] = word

                elif i > 0 and "кут" in significant_words[i - 1]:
                    task_data['angle'] = word

                elif i > 0 and "діагональ" in significant_words[i - 1]:
                    task_data['diagonal'] = word

        return {key: value for key, value in task_data.items() if value is not None}

class GeometryTaskExtractor(TaskExtractor):
    @staticmethod
    def analyze_task_question(task_question, task_data):

        keyword_to_property = {
            'висота': 'height',
            'бічний сторона': 'side',
            'периметр': 'perimeter',
            'площа': 'area',
            'більший основа': 'bigger base',
            'менший основа': 'smaller base',
            'основа': 'bases',
            'кут': 'angles',
            'діагоналя': 'diagonal',
            'середній лінія': 'middle line',
            'невідомо': 'undefined'
        }

        for keyword, property_name in keyword_to_property.items():
            if keyword in task_question.lower():
                return property_name

        english_letter_regex = re.compile(r'\b[a-z]\b')
        match = english_letter_regex.search(task_question.lower())
        if match:
            letter = match.group(0)
            for key, value in task_data.items():
                if value == letter:
                    task_data[key] = None
                    return key

        return "undefined"


if __name__ == "__main__":
    tasks = TaskExtractor.load_tasks_from_excel()
    if tasks:
        for i in range(len(tasks)):
           text = tasks[i]
           processed_text = TextPreprocessor.preprocess(text)
           udpipe_result = UDPipeAPI.process_text(processed_text)
           significant_words = UDPipeAPI.extract_significant_words(udpipe_result)
           task_condition, task_question = UDPipeAPI.split_task(" ".join(significant_words))
           print("Task condition:", tasks[i])

           task_data = GeometryTaskAnalyser.get_task_data(significant_words)
           #print("Data:", task_data)

           task_undefined = GeometryTaskExtractor.analyze_task_question(task_question, task_data)
           #print("Undefined:", task_undefined)

           result = Solver.solve_geometry_task(task_data, task_undefined)
           print("Result:\n", result[1])

           Solver.draw_trapezoid(task_data, task_undefined, result)
           print("\n")