# メソッドを使用したクラス
class Student():
  def set_data(self, name, height, weight):
    self.name = name
    self.height = height
    self.weight = weight
  
  # 自己紹介するメソッド
  def say_my_data(self):
    print("I am {}. My height is {}cm. My weight is {}kg.".format(self.name, self.height, self.weight))


  # BMIと適正体重を言うメソッド
  def my_BMI(self):
    bmi = round(self.weight /(self.height/100.)**2)
    best_weight = round((self.height/100.)**2 * 22)
    print("My BMI is {}. My BEST weight is {} kg.".format(bmi, best_weight))

student1 = Student() # インスタンスを作成
student1.set_data("matsuzaka", 183, 93) # 属性を一気に設定

student1.say_my_data()
student1.my_BMI()