import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout)
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name: ", self)
        self.input_city = QLineEdit(self)
        self.getweather_button = QPushButton("Get Weather🌞🌞", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.condtion_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.input_city)
        vbox.addWidget(self.getweather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.condtion_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.input_city.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.condtion_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("City_Label")
        self.input_city.setObjectName("City_Input")
        self.getweather_button.setObjectName("Get_Weather")
        self.temperature_label.setObjectName("Temperature")
        self.condtion_label.setObjectName("Weather_Condition")
        self.emoji_label.setObjectName("Emoji")

        self.setStyleSheet(
            """    QPushButton,QLabel{
                font-family: New Times Roman;
            } 
            QLabel#City_Label{
                font-size : 30px;
                font-style : italic;
                }         
            QLineEdit#City_Input{
                font-size : 20px;
            }
            QPushButton#Get_Weather{
                font-size :20px;
                font-style :bold;
            }
            QLabel#Temperature{
                font-size :70px;
                font-style:bold;
            }
            QLabel#Emoji{
                font-size:100px;
                font-family: Segoe UI emoji;
            }
            QLabel#Weather_Condition{
                font-size:50px;
                font-style:bold;
            }
                """
        )

        self.getweather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "d949575735adeed74f229346fccb6e0b"
        city = self.input_city.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error(
                        "Invalid input , please check your input")
                case 401:
                    self.display_error("Invalid API Key Check Again, ")
                case 403:
                    self.display_error("Region not mapped in our Database")
                case 404:
                    self.display_error("City doesnt exists")
                case 500:
                    self.display_error(
                        "CIty is on an extra terestrial planet ")
                case 502:
                    self.display_error("Who the fuck is that guy ")
                case 503:
                    self.display_error("The fuck is a city")
                case 504:
                    self.display_error("baseball huh")
                case _:
                    self.display_error("You done fucked my nigga")
        except requests.exceptions.RequestException:
            self.display_error("Get your money up not your funny up lil nigga")
        except requests.exceptions.Timeout:
            self.display_error("Damn foo you timed out")
        except requests.exceptions.ConnectionError:
            self.display_error(
                "who is gonna connect to the surce my nigga ? your grandma?")
        except requests.exceptions.TooManyRedirects:
            self.display_error("You getting redirecting lil shit")

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size:70px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273
        self.temperature_label.setText(f"{temperature_c:.0f} C")
        condition = data["weather"][0]["description"]
        self.condtion_label.setStyleSheet("font-size:30px")
        self.condtion_label.setText(f"{condition}")
        weather_id = data["weather"][0]["id"]
        self.emoji_label.setText(self.weather_emoji(weather_id))

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size:20px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()

    @staticmethod
    def weather_emoji(weather_id):
        if 200 <= weather_id <= 230:
            return "🌞"
        elif 300 <= weather_id <= 330:
            return "☁️"
        elif 500 <= weather_id <= 530:
            return "🌦️"
        elif 600 <= weather_id <= 630:
            return "⛈️"
        elif 700 <= weather_id <= 720:
            return "❄️"
        elif weather_id == 730:
            return "⛄"
        else:
            return "🫢"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
