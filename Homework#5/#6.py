final_dict = {}
with open('text#6') as file:
    for line in file:
        l_type, *lessons = line.split()
        l_count = [int(lesson.rstrip('(л)(пр)(лаб)')) for lesson in lessons if lesson != '-']
        final_dict.update({l_type.rstrip(':') : sum(l_count)})
print(final_dict)