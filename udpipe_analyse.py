import requests
import re
import pandas as pd


class TaskExtractor:
    @staticmethod
    def load_tasks_from_excel(file_path = "bank_zadach_trapeziya.xlsx", column_name="Умова задачі"):
        try:
            df = pd.read_excel(file_path)
            if column_name not in df.columns:
                raise ValueError(f"Column '{column_name}' not found in the file.")
            tasks = df[column_name].dropna().tolist()
            return tasks
        except Exception as e:
            raise Exception(f"Error reading Excel file: {e}")


class TextPreprocessor:
    @staticmethod
    def preprocess(raw_text):
        modified_text = re.sub(r'\bвідстань між основами\b', 'висота', raw_text)
        cleaned_text = re.sub(r'[^\w\s]', '', modified_text)
        normalized_text = cleaned_text.lower()
        standardized_text = TextPreprocessor.expand_abbreviations(normalized_text)
        reordered_text = TextPreprocessor.move_condition_to_start(standardized_text)
        return reordered_text

    @staticmethod
    def expand_abbreviations(text):
        abbreviations = {
            "мм": "міліметри",
            "см": "сантиметри",
            "дм": "дециметри",
            "м": "метри",
            "км": "кілометри"
        }

        for abbreviation, full_form in abbreviations.items():
            text = re.sub(rf'\b{abbreviation}\b', full_form, text)
        return text

    @staticmethod
    def move_condition_to_start(text):
        if_match = re.search(r'\bякщо\b.*?(?=[.?!]|$)', text)
        if if_match:
            condition = if_match.group(0).strip()
            remaining_text = text.replace(condition, '').strip()
            reordered_text = f"{condition}, {remaining_text}"
            return reordered_text.strip(", ")
        return text



class UDPipeAPI:
    BASE_URL = "https://lindat.mff.cuni.cz/services/udpipe/api/"

    @staticmethod
    def process_text(text, model="ukrainian", tokenizer=True, tagger=True, parser=True):
        params = {
            "data": text,
            "model": model,
            "tokenizer": "" if tokenizer else None,
            "tagger": "" if tagger else None,
            "parser": "" if parser else None,
        }
        response = requests.post(UDPipeAPI.BASE_URL + "process", data=params)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error processing text: {response.status_code}")

    @staticmethod
    def extract_significant_words(udpipe_result):
        result_lines = udpipe_result["result"].split("\n")
        significant_words = []

        synonyms = {
            "шукати": "знайти",
            "знайти": "знайти",
            "виявити": "знайти",
            "пошукати": "знайти",
            "пошук": "знайти",
            "відшукати": "знайти",
            "визначити": "знайти",
            "зрозуміти": "знайти",
            "обчислити": "знайти",
            "обрахувати": "знайти",
            "обчисліти": "знайти"

        }

        words_to_exclude = {"мати", "довжина", "дорівнювати", "трапеція", "рівнобічний", "рівнобедрений"}

        for line in result_lines:
            if line and not line.startswith("#"):
                columns = line.split("\t")
                if len(columns) > 3:
                    word = columns[2]
                    pos_tag = columns[3]
                    if pos_tag in {"NOUN", "NUM", "VERB", "ADJ", "SYM"}:
                        word = synonyms.get(word, word)
                        if word not in words_to_exclude:
                            significant_words.append(word)

        return significant_words

    @staticmethod
    def split_task(task):
        try:
            find_index = task.index("знайти")
            condition = task[:find_index]
            question = task[find_index:]
            return condition, question
        except ValueError:
            return task, []





if __name__ == "__main__":
    tasks = TaskExtractor.load_tasks_from_excel()
    print("Loaded tasks:", tasks)

    if tasks:
        for i in range(len(tasks)):
            text = tasks[i]
            processed_text = TextPreprocessor.preprocess(text)

            result = UDPipeAPI.process_text(processed_text)

            significant_words = UDPipeAPI.extract_significant_words(result)
            task_condition, task_question = UDPipeAPI.split_task(significant_words)

            #print("Processed text:", processed_text)
            #print("Processed result:\n", result["result"])
            #print("Significant words:", significant_words)
            print(text)
            print("Task condition:", task_condition)
            print("Task question:", task_question)
            print("\n\n")