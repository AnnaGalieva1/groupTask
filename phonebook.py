#Вывод справочника на экран.
def displaying_the_phone_directory_on_the_screen(file_csv):
    with open(file_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['id'], row['First_Name'], row['Last_Name'], 
            row['Number'], row['Description'])