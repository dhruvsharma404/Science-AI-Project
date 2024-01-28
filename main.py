import customtkinter
from PIL import Image
import random
from openai import OpenAI
client = OpenAI(api_key="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")
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("290x300")
app.title("AI Stomata Counter")
app.iconbitmap('image (1).ico')
app.resizable(False, False)

def image():
    im = Image.open("stomata.png")
    angle = random.randint(90, 180)
    out = im.rotate(angle)
    out.save("stomata.png")

    my_image = customtkinter.CTkImage(light_image=Image.open("stomata.png"),
                                    dark_image=Image.open("stomata.png"),
                                    size=(160, 160))

    image_label = customtkinter.CTkLabel(app, image=my_image, text="")
    image_label.place(x=65, y=10)

image()

def button_function():
    image()

    plantget = str(plant.get("0.0", "end"))
    print(plantget)

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": r"You need to give an answer without any explanation, or unnecessary things, but it has to be 100% accurate. It has to be the correct answer. You can get information from Wikipedia or other sites. Giving wrong answers is inacceptable. The answer should be in this format: Approximately {approximate number of stomata} stomata" },{"role": "user", "content": "How many stomata are in a " + plantget + " plant's leaf on average?"}],
        stream=True,
    )
    answer = []
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            answer.append(chunk.choices[0].delta.content)
    final = "".join(str(e) for e in answer)
    label.configure(text=final)



plant = customtkinter.CTkTextbox(app, width=180, height=2, font=("Single Day", 20))
plant.place(x=80, y=200)
plant['wrap'] = 'none'
enter = customtkinter.CTkButton(master=app, text="Check number of stomata", width=230, font=("Single Day", 20), command=button_function)
enter.place(x=30, y=240)
label = customtkinter.CTkLabel(app, text="Approximately 100,000 stomata", font=("Single Day", 20))
label.place(relx=0.5, y=185, anchor=customtkinter.CENTER)
stomatas = customtkinter.CTkLabel(app, text="Number", font=("Single Day", 20))
stomatas.configure(text= "Plant:")
stomatas.place(x=30, y=205)
app.mainloop()