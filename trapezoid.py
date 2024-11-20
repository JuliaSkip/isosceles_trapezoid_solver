import math
import matplotlib.pyplot as plt

# периметр, більша основа, бічна сторона - менша основа
def smaller_base_by_perimeter_bigger_base_side(perimeter, bigger_base, side):
    result = perimeter - bigger_base - (side * 2)
    text = ("Дано:\n"
            f'P = {perimeter}\n'
            f'AD = {bigger_base}\n'
            f'AB = CD = {side}\n'
            "Знайдемо меншу основу.\n"
            "BC = P - AD - (AB + CD)\n"
            f'BC = {perimeter} - {bigger_base} - ( {side} + {side} )\n'
            f'Відповідь: {result}')
    return result, text

# більша основа, висота, бічна сторона - менша основа
def smaller_base_with_bigger_base_height_side(bigger_base, height, side):
    result1 = 2 * math.sqrt(side ** 2 - height ** 2)
    result = bigger_base - result1
    text = ("Дано:\n"
            f'AD = {bigger_base}\n'
            f'AB = CD = {side}\n'
            f'BK = {height}\n'
            "Знайдемо меншу основу.\n"
            "BC = AD - ( 2 * sqrt( AB^2 - BK^2 ) )\n"
            f'BC = {bigger_base} - ( 2 * sqrt( {side}^2 + {height}^2 ) )\n'
            f'Відповідь: {result1}'
            )
    return result, text

# більша основа, висота, бічна сторона - периметр
def perimeter_with_height_and_side(bigger_base, height, side):
    result1 = smaller_base_with_bigger_base_height_side(bigger_base, height, side)
    result = bigger_base + result1[0] + (2 * side)
    text = ("Дано:\n"
            f'AD = {bigger_base}\n'
            f'AB = CD = {side}\n'
            f'BK = {height}\n'
            "Знайдемо меншу основу.\n"
            "BC = AD - ( 2 * sqrt( AB^2 - BK^2 ) )\n"
            f'BC = {bigger_base} - ( 2 * sqrt( {side}^2 + {height}^2 ) )\n'
            "Знайдемо периметр\n"
            "P = AD + BC + 2 * AB\n"
            f"P = {bigger_base} + {result1[0]} + 2 * {side}\n"
            f"Відповідь: {result}")

    return result, text

# більша основа, менша основа, бічна сторона - периметр
def perimeter_with_bases_and_side(bigger_base, smaller_base, side):
    result = bigger_base + smaller_base + (2 * side)
    text = ("Дано:\n"
            f'AD = {bigger_base}\n'
            f'BC = {smaller_base}\n'
            f'AB = CD = {side}\n'
            "Знайдемо периметр."
            "P = AD + BS + AB + CD\n"
            f'P = {bigger_base} + {smaller_base} + {side} + {side}\n '
            f"Відповідь: {result}")

    return result, text

# більша основа, менша основа, висота - периметр
def perimetr_with_bases_and_height(bigger_base, smaller_base, height):
    result1 = math.sqrt(((bigger_base - smaller_base) / 2) ** 2 + height ** 2)
    result = bigger_base + smaller_base + 2 * result1
    text = ("Дано:\n"
            f"AD = {bigger_base}\n"
            f"BC = {smaller_base}\n"
            f"BK = {height}\n"
            "Знайдемо бічну сторону.\n"
            "AB = sqrt(((AD - BC) / 2)^2 + BK^2)\n"
            f"AB = sqrt((({bigger_base} - {smaller_base}) / 2)^2 + {height}^2)\n"
            f"AB = CD = {result1}\n"
            "Знайдемо периметр.\n"
            "P = AD + BC + CD + AB\n"
            f"P = {bigger_base} + {smaller_base} + {result1} + {result1} \n"
            f"Відповідь: {result}")
    return result, text

# бічна сторона, більша основа, кут - середня лінія
def middle_line_by_side_base_angle(side, bigger_base, angle):
    result1 = math.ceil(bigger_base - 2 * side * math.cos(math.radians(angle)))
    result = (bigger_base + result1) / 2
    text = ("Дано:\n"
            f"AB = CD = {side}\n"
            f"AD = {bigger_base}\n"
            f"∠a = {angle}°\n"
            "MN = (AD + BC) / 2\n"
            "Знайдемо меншу основу.\n"
            "BC = AD - 2 * AB * cos(∠a)\n"
            f"BC = {bigger_base} - 2 * {side} * cos({angle}°)\n"
            f'BC = {result1}\n'
            "Знайдемо середню лінію.\n"
            f"MN = ({bigger_base} + {result1}) / 2\n"
            f"MN = {result}\n"
            f'Відповідь:{result}')
    return result, text

# висота, більша основа - бічна сторона
def side_by_height_and_bigger_base(height, bigger_base, smaller_base):
    result1 = (bigger_base - smaller_base) / 2
    result = math.sqrt(result1 ** 2 + height ** 2)
    text = ("Дано:\n"
            f"BK = {height}\n"
            f"AK = {result1}\n"
            f"KD = {bigger_base - result1}\n"
            "Знайдемо бічну сторону(за теоремою Піфагора)\n"
            "AB = sqrt(AK^2 + BK^2)\n"
            f"AB = sqrt({result1}^2 + {height}^2)\n"
            f"AB = {result}\n"
            f'Відповідь:{result}')
    return result, text

# периметр, більша основа, менша основа - бічна сторона
def side_by_perimeter_and_bases(perimeter, bigger_base, smaller_base):
    result = (perimeter - bigger_base - smaller_base) / 2
    text = ("Дано:\n"
            f"P = {perimeter}\n"
            f"AD = {bigger_base}\n"
            f"BC = {smaller_base}\n"
            "Знайдемо бічну сторону.\n"
            "AB = CD = (P - AD - BC) / 2\n"
            f"AB = CD = ({perimeter} - {bigger_base} - {smaller_base}) / 2\n"
            f"AB = CD = {result}\n"
            f'Відповідь:{result}')
    return (result, text)

# менша основа, більша основа, бічна сторона - висота
def height_by_bases_and_side(smaller_base, bigger_base, side):
    x = (bigger_base - smaller_base) / 2
    height = math.sqrt(side ** 2 - x ** 2)

    text = ("Дано:\n"
            f"BC = {smaller_base}\n"
            f"AD = {bigger_base}\n"
            f"AB = CD = {side}\n"
            "Знайдемо відрізок AK\n"
            "AK = (AD - BC) / 2\n"
            f"AK = ({bigger_base} - {smaller_base}) / 2\n"
            f"AK = {x}\n"
            "Знайдемо висоту(за теоремою Піфагора).\n"
            "BK = sqrt(AB^2 - AK^2)\n"
            f"BK = sqrt({side}^2 - {x}^2)\n"
            f"BK = {height}\n"
            f'Відповідь:{height}')
    return height, text

# різниця протилежних кутів - кути
def angles_by_angles_diff(angles_diff):
    alpha = (180 + angles_diff) / 2
    beta = 180 - alpha
    text = ("Дано:\n"
            f"Різниця протилежних кутів: Δ = {angles_diff}°\n"
            "Знайдемо кути трапеції.\n"
            "α = (180 + Δ) / 2\n"
            "β = 180 - α\n"
            f"α = (180 + {angles_diff}) / 2 = {alpha}°\n"
            f"β = 180 - {alpha} = {beta}°\n"
            "Відповідь:\n"
            f"∠A = ∠D = {alpha}°\n"
            f"∠B = ∠C = {beta}°")
    return (alpha, beta, alpha, beta), text

# кут, бічна сторона, сума основ - основи
def find_bases_by_angle_side_sum_bases(angle, side, sum_bases):
    angle_rad = math.radians(angle)
    x = math.ceil( side * math.cos(angle_rad))
    a = (sum_bases / 2) + x
    b = sum_bases - a

    text = ("Дано:\n"
            f"∠a = {angle}°\n"
            f"AB = CD = {side}\n"
            f"SUM = AD + BC = {sum_bases}\n"
            "Знайдемо основи трапеції.\n"
            "Знайдемо проєкцію бічної сторони на горизонтальну вісь (AK):\n"
            "AK = AB * cos(∠a)\n"
            f"AK = {side} * cos({angle}°) = {x}\n"
            "Знайдемо більшу основу.\n"
            "AD = SUM / 2 + AK\n"
            f"AD = ({sum_bases} / 2) + {x}\n"
            f"AD = {a}\n"
            "Знайдемо меншу основу.\n"
            "BC = SUM - AD\n"
            f"BC = {sum_bases} - {a}\n"
            f"BC = {b}\n"
            "Відповідь:\n"
            f"AD = {a}\n"
            f"BC= {b}")

    return (a, b), text

# кут - кути
def angle_by_angles(angle):
    remaining_angle = 180 - angle
    text = ("Дано:\n"
            f"∠a = {angle}°\n"
            "Знайдемо решту кутів.\n"
            "У рівнобічній трапеції сума суміжних кутів дорівнює 180°:\n"
            "∠b = 180° - ∠a\n"
            f"∠b = 180 - {angle}\n"
            f"∠b = {remaining_angle}°\n"
            "Відповідь:\n"
            f"Кути: {angle}°, {remaining_angle}°, {angle}°, {remaining_angle}°")

    return (angle, remaining_angle, angle, remaining_angle), text

# більша основа, менша основа, висота - площа
def area_by_bases_and_height(bigger_base, smaller_base, height):
    area = ((smaller_base + bigger_base) / 2) * height
    text = ("Дано:\n"
            f"AD = {bigger_base}\n"
            f"BC = {smaller_base}\n"
            f"BK = {height}\n"
            "Знайдемо площу трапеції.\n"
            "S = ((AD + BC) / 2) * BK\n"
            f"S = (({bigger_base} + {smaller_base}) / 2) * {height}\n"
            f"S = {area}\n"
            f"Відповідь:{area}")
    return area, text

# середня лінія, висота	- площа
def area_by_middle_line_and_height(middle_line, height):
    area = middle_line * height
    text = ("Дано:\n"
            f"MN = {middle_line}\n"
            f"BK = {height}\n"
            "Знайдемо площу трапеції.\n"
            "S = MN * BK\n"
            f"S = {middle_line} * {height}\n"
            f"S = {area}\n"
            f"Відповідь:{area}")
    return area, text

# середня лінія, менша основа - більша основа
def base_by_middle_line_and_base(middle_line, base):
    res = ((2 * middle_line) - base)
    text = ("Дано:\n"
            f"MN = {middle_line}\n"
            f"base = {base}\n"
            "Знайдемо іншу основу.\n"
            "base2 = (2 * MN) - base\n"
            f"base2 = (2 * {middle_line}) - {base}\n"
            f"base2 = {res}\n"
            f"Відповідь:{res}")
    return res, text

def bigger_base_by_diagonal_height_and_base(diagonal, height, base):
    a = math.sqrt(diagonal ** 2 - height ** 2)
    b = a - base
    res = a + b
    text = ("Дано:\n"
            f"AC = BD = {diagonal}\n"
            f"BK = {height}\n"
            f"base = {base}\n"
            "Знайдемо відстань від проекції діагоналі до іншої основи.\n"
            "a = sqrt(AC^2 - BK^2)\n"
            f"a = sqrt({diagonal}^2 - {height}^2)\n"
            f"a = {a}\n"
            "Знайдемо іншу основу.\n"
            "b = a - base\n"
            f"b = {a} - {base} "
            f"b = {b}\n"
            "base2 = a + b\n"
            f"base2 = {a + b}\n"
            f"Відповідь:{res}")
    return res, text

# сума основ - бічна сторона
def side_by_sum_bases(sum_bases):
    side = (sum_bases / 2)
    text = ("Дано:\n"
            f"SUM = {sum_bases}\n"
            "Знайдемо бічну сторону(за властивістю сторін рівнобедреної трапеції).\n"
            "AB = CD = SUM / 2\n"
            f"AB = CD = {sum_bases} / 2 = {side}\n"
            f"Відповідь:{side}")
    return side, text

def bases(bigger_base, smaller_base):
    ak = ((bigger_base - smaller_base) / 2)
    kd = bigger_base - ak
    text = ("Дано:\n"
            f"AK = {ak}\n"
            f"KD = {kd}\n"
            "Знайдемо основи.\n"
            "AD = AK + KD\n"
            f"AD = {ak} - {kd}\n"
            f"AD = {bigger_base}\n"
            "BC = KD - AK\n"
            f"BC = {kd} - {ak}\n"
            f"BC = {smaller_base}\n"
            f"Відповідь:{(bigger_base, smaller_base)}")
    return (bigger_base, smaller_base), text



class Solver:

    @staticmethod
    def solve_geometry_task(task_data, task_undefined):

        task_data = {key: value for key, value in task_data.items() if isinstance(value, (int, float)) or (isinstance(value, str) and value.replace('.', '', 1).isdigit())}
        task_data = {key: float(value) for key, value in task_data.items()}

        if task_undefined == 'bases' and 'smaller base' in task_data and 'bigger base' in task_data:
            return bases(task_data['bigger base'], task_data['smaller base'])

        if task_undefined == 'smaller base' and 'bigger base' in task_data and 'middle line' in task_data:
            return base_by_middle_line_and_base(task_data['middle line'], task_data['bigger base'])

        if task_undefined == 'bigger base' and 'smaller base' in task_data and 'middle line' in task_data:
            return base_by_middle_line_and_base(task_data['middle line'], task_data['smaller base'])

        if task_undefined == 'bigger base' and 'smaller base' in task_data and 'height' in task_data and 'diagonal' in task_data:
            return bigger_base_by_diagonal_height_and_base(task_data['diagonal'], task_data['height'], task_data['smaller base'])

        if task_undefined == 'smaller base' and 'perimeter' in task_data and 'bigger base' in task_data and 'side' in task_data:
            return smaller_base_by_perimeter_bigger_base_side(task_data['perimeter'], task_data['bigger base'], task_data['side'])

        if task_undefined == 'smaller base' and 'bigger base' in task_data and 'height' in task_data and 'side' in task_data:
            return smaller_base_with_bigger_base_height_side(task_data['bigger base'], task_data['height'], task_data['side'])

        if task_undefined == 'perimeter' and 'bigger base' in task_data and 'height' in task_data and 'side' in task_data:
            return perimeter_with_height_and_side(task_data['bigger base'], task_data['height'], task_data['side'])

        if task_undefined == 'perimeter' and 'bigger base' in task_data and 'smaller base' in task_data and 'side' in task_data:
            return perimeter_with_bases_and_side(task_data['bigger base'], task_data['smaller base'], task_data['side'])

        if task_undefined == 'perimeter' and 'bigger base' in task_data and 'smaller base' in task_data and 'height' in task_data:
            return perimetr_with_bases_and_height(task_data['bigger base'], task_data['smaller base'], task_data['height'])

        if task_undefined == 'middle line' and 'side' in task_data and 'bigger base' in task_data and 'angle' in task_data:
            return middle_line_by_side_base_angle(task_data['side'], task_data['bigger base'], task_data['angle'])

        if task_undefined == 'side' and 'height' in task_data and 'bigger base' in task_data and 'smaller base' in task_data:
            return side_by_height_and_bigger_base(task_data['height'], task_data['bigger base'], task_data['smaller base'])

        if task_undefined == 'side' and 'perimeter' in task_data and 'bigger base' in task_data and 'smaller base' in task_data:
            return side_by_perimeter_and_bases(task_data['perimeter'], task_data['bigger base'], task_data['smaller base'])

        if task_undefined == 'side' and 'sum bases':
            return side_by_sum_bases(task_data['sum bases'])

        if task_undefined == 'height' and 'smaller base' in task_data and 'bigger base' in task_data and 'side' in task_data:
            return height_by_bases_and_side(task_data['smaller base'], task_data['bigger base'], task_data['side'])

        if task_undefined == 'angles' and 'diff angles' in task_data:
            return angles_by_angles_diff(task_data['diff angles'])

        if task_undefined == 'bases' and 'angle' in task_data and 'side' in task_data and 'sum bases' in task_data:
            return find_bases_by_angle_side_sum_bases(task_data['angle'], task_data['side'], task_data['sum bases'])

        if task_undefined == 'angles' and 'angle' in task_data:
            return angle_by_angles(task_data['angle'])

        if task_undefined == 'area' and 'smaller base' in task_data and 'bigger base' in task_data and 'height' in task_data:
            return area_by_bases_and_height(task_data['bigger base'], task_data['smaller base'], task_data['height'])

        if task_undefined == 'area' and 'middle line' and 'height' in task_data:
            return area_by_middle_line_and_height(task_data['middle line'], task_data['height'])


        else:
            return "Task cannot be solved with the given data."


    @staticmethod
    def is_valid_number(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def draw_trapezoid(task_data, task_undefined, result):
        try:
            task_data = {key: value for key, value in task_data.items() if value is not None and Solver.is_valid_number(value)}

            bigger_base = task_data.get('bigger base', '?')
            smaller_base = task_data.get('smaller base', '?')
            height = task_data.get('height', '?')

            if bigger_base == '?' and smaller_base != '?':
                bigger_base = float(smaller_base) * 2
            elif bigger_base == '?':
                bigger_base = 20

            if smaller_base == '?' and bigger_base != '?':
                smaller_base = float(bigger_base) / 2
            elif smaller_base == '?':
                smaller_base = 10

            if height == '?':
                height = 6

            if 'circle' in task_data and task_data['circle'] is not None:
                bigger_base = 18
                smaller_base = 6
                height = 10

            bigger_base = float(bigger_base)
            smaller_base = float(smaller_base)
            height = float(height)

            x1, y1 = 0, 0 # A
            x2, y2 = bigger_base, 0 # D
            x3, y3 = (bigger_base - smaller_base) / 2, height # B
            x4, y4 = x3 + smaller_base, height # C

            plt.figure(figsize=(10, 8))
            plt.plot([x1, x2, x4, x3, x1], [y1, y2, y4, y3, y1], 'b-', label="Trapezoid")
            plt.fill([x1, x2, x4, x3], [y1, y2, y4, y3], 'skyblue', alpha=0.5)

            if task_undefined == 'height' or 'height' in task_data or 'height present' in task_data or 'height':
                hx1, hy1 = x3, y3
                hx2, hy2 = x3, y1
                plt.plot([hx1, hx2], [hy1, hy2], 'g--', label="Height")
                plt.text(x3 + 0.2, y1 - 0.7, "K", fontweight="bold", fontsize=15, ha='right')

            mx1, my1 = (x1 + x3) / 2, (y1 + y3) / 2
            mx2, my2 = (x2 + x4) / 2, (y2 + y4) / 2

            if task_undefined == 'middle line' or 'middle line' in task_data:
                plt.plot([mx1, mx2], [my1, my2], 'c--', label="Middle Line")
                plt.text((x1 + x3) / 2 - 0.2, (y1 + y3) / 2, "M", fontweight="bold", fontsize=15, ha='right')
                plt.text((x2 + x4) / 2 + 0.7, (y2 + y4) / 2, "N", fontweight="bold", fontsize=15, ha='right')

            if task_undefined == 'diagonal' or 'diagonal' in task_data:
                plt.plot([x1, x4], [y1, y4], 'm--', label="Diagonal 1")
                plt.plot([x2, x3], [y2, y3], 'm--', label="Diagonal 2")

            plt.text(x1 - 0.2, y1, "A", fontweight="bold", fontsize=15, ha='right')
            plt.text(x3 + 0.2, y3 + 0.2, "B", fontweight="bold", fontsize=15, ha='right')
            plt.text(x4 + 0.2, y4 + 0.2, "C", fontweight="bold", fontsize=15, ha='right')
            plt.text(x2 + 0.5, y2, "D", fontweight="bold", fontsize=15, ha='right')



            # Defined
            if 'circle' in task_data and task_data['circle'] is not None:
                circle = plt.Circle(((mx1+mx2) / 2, (my1 + my2) / 2), (height/2), color='red', alpha=0.3)
                plt.gca().add_patch(circle)

            if 'bigger base' in task_data and task_data['bigger base'] is not None and 'bigger base small' not in task_data:
                plt.text((x1 + x2) / 2, 0.5, task_data['bigger base'], ha='center', fontsize=15, color='b')

            if 'bigger base' in task_data and task_data['bigger base'] is not None and 'bigger base small' in task_data:
                plt.text((x1 + x3) / 2, 0.5, task_data['bigger base small'], ha='center', fontsize=15, color='c')
                plt.text((x1 + x2) / 2, 0.5, task_data['bigger base large'], ha='center', fontsize=15, color='b')
                plt.plot([x1, x3], [y1, y1], 'c')

            if 'smaller base' in task_data and task_data['smaller base'] is not None and 'bigger base small' not in task_data:
                plt.text((x3 + x4) / 2, height - 1,  task_data['smaller base'], ha='center', fontsize=15, color='b')

            if 'height' in task_data and task_data['height'] is not None:
                plt.text(x3 - 1, height / 2 - 1, task_data['height'], va='center', fontsize=15, color='g')

            if 'sum bases' in task_data and task_data['sum bases'] is not None:
                sum = task_data['sum bases']
                plt.xlabel(f'Sum of bases: {sum}', fontsize=15, color='g', fontweight='bold')

            if 'side' in task_data and task_data['side'] is not None:
                plt.text(x1, height / 2, task_data['side'], va='center', fontsize=15, color='b')
                plt.text(x2, height / 2, task_data['side'], va='center', fontsize=15, color='b')

            if 'perimeter' in task_data and task_data['perimeter'] is not None:
                perimeter = task_data['perimeter']
                plt.xlabel(f'Perimeter: {perimeter}', fontsize=15, color='g', fontweight='bold')

            if 'area' in task_data and task_data['area'] is not None:
                area = task_data['area']
                plt.xlabel(f'Area: {area}', fontsize=15, color='g', fontweight='bold')

            if 'angle' in task_data and task_data['angle'] is not None:
                angle = task_data['angle']
                if float(angle) > 90:
                    plt.text(x3 - 2.3, y3 - 1, f'{angle}°', fontsize=15, color='b')
                    plt.text(x4 + 1, y4 - 1, f'{angle}°', fontsize=15, color='b')
                else:
                    plt.text(x1 - 0.5, y1 + 1, f'{angle}°', fontsize=15, color='b')
                    plt.text(x2, y2 + 1, f'{angle}°', fontsize=15, color='b')

            if 'sum angles' in task_data and task_data['sum angles'] is not None:
                sum_angles = task_data['sum angles']
                plt.xlabel(f'Sum Angles: {sum_angles}', fontsize=15, color='g', fontweight='bold')

            if 'diff angles' in task_data and task_data['diff angles'] is not None:
                diff_angles = task_data['diff angles']
                plt.xlabel(f'Diff Angles: {diff_angles}',fontsize=15, color='g', fontweight='bold')

            if 'middle line' in task_data and task_data['middle line'] is not None:
                plt.text((x4 + x3) / 2 - 0.5 , height / 2 + 0.5, task_data['middle line'], fontsize=15, color='c', fontweight='bold')

            if 'diagonal' in task_data and task_data['diagonal'] is not None:
                plt.text((x4 + x3) / 2 + 2 , height / 2 + 0.5, task_data['diagonal'], fontsize=15, color='m', fontweight='bold')
                plt.text((x4 + x3) / 2 - 2 , height / 2 + 0.5, task_data['diagonal'], fontsize=15, color='m', fontweight='bold')


            # Undefined
            if task_undefined:
                if 'bigger base' in task_undefined:
                    plt.text((x1 + x2) / 2, -1, "?", fontsize=15, color='red')
                    plt.plot([x1, x2], [y1, y2], 'r')

                if 'smaller base' in task_undefined:
                    plt.text((x3 + x4) / 2, height + 0.2, "?", fontsize=15, color='red')
                    plt.plot([x3, x4], [y3, y4], 'r')

                if 'bases' in task_undefined:
                    plt.text((x1 + x2) / 2, -1, "?", fontsize=15, color='red')
                    plt.plot([x1, x2], [y1, y2], 'r')
                    plt.text((x3 + x4) / 2, height + 0.2, "?", fontsize=15, color='red')
                    plt.plot([x3, x4], [y3, y4], 'r')

                if 'height' in task_undefined:
                    plt.text(x3 - 1, height / 2 - 1, "?", fontsize=15, color='red')
                    plt.plot([hx1, hx2], [hy1, hy2], 'r--', label="Height")

                if 'sum bases' in task_undefined:
                    plt.xlabel('Sum bases?', fontsize=15, color='red', fontweight='bold')

                if 'side' in task_undefined:
                    plt.text(x1, height / 2, "?", fontsize=15, color='red')
                    plt.text(x2, height / 2, "?", fontsize=15, color='red')
                    plt.plot([x1, x3], [y1, y3], 'r')
                    plt.plot([x4, x2], [y4, y2], 'r')

                if 'perimeter' in task_undefined:
                    plt.xlabel('Perimeter?', fontsize=15, color='red', fontweight='bold')
                    plt.plot([x1, x2, x4, x3, x1], [y1, y2, y4, y3, y1], 'r', label="Trapezoid")

                if 'area' in task_undefined:
                    plt.xlabel('Area?', fontsize=15, color='red')
                    plt.fill([x1, x2, x4, x3], [y1, y2, y4, y3], 'red', alpha=0.5)

                if 'angle' in task_undefined and ('sum angles' in task_data or 'diff angles' in task_data):
                    plt.text(x3 - 1.5, y3 - 1, "?", fontsize=15, color='red')
                    plt.text(x4 + 1, y4 - 1, "?", fontsize=15, color='red')
                    plt.text(x1, y1 - 1, "?", fontsize=15, color='red')
                    plt.text(x2 - 1, y2 - 1, "?", fontsize=15, color='red')
                elif 'angle' in task_undefined:
                    if float(result[0][0]) < 90:
                        plt.text(x3 - 1.5, y3 - 1, "?", fontsize=15, color='red')
                        plt.text(x4 + 1, y4 - 1, "?", fontsize=15, color='red')
                    else:
                        plt.text(x1, y1 - 1, "?", fontsize=15, color='red')
                        plt.text(x2 - 1, y2 - 1, "?", fontsize=15, color='red')

                if 'sum angles' in task_undefined:
                    plt.xlabel('Sum of angles?', fontsize=15, color='red', fontweight='bold')

                if 'diff angles' in task_undefined:
                    plt.xlabel('Difference of angles?', fontsize=15, color='red', fontweight='bold')

                if 'middle line' in task_undefined:
                    plt.text((x4 + x3) / 2 - 0.5 , height / 2 + 0.5, "?", fontsize=15, color='red')
                    plt.plot([mx1, mx2], [my1, my2], 'r--', label="Middle Line")

                if 'diagonal' in task_undefined:
                    plt.text((x4 + x3) / 2 + 2 , height / 2 + 0.5, "?", fontsize=15, color='r', fontweight='bold')
                    plt.text((x4 + x3) / 2 - 2 , height / 2 + 0.5, "?", fontsize=15, color='r', fontweight='bold')
                    plt.plot([x1, x4], [y1, y4], 'r--', label="Diagonal 1")
                    plt.plot([x2, x3], [y2, y3], 'r--', label="Diagonal 2")


            plt.axis('equal')
            plt.show()

        except ValueError:
            print("Error in the data format while drawing the trapezoid.")
