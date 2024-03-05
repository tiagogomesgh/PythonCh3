### Tiago Gomes - COP 1000 #1284
###

### Psuedocode
### PROMPT the user to enter 3 seperate blood sugar readings as mg/dL.
### CREATE an IF statement, using booleans to determine the highest blood sugar reading.
### WITHIN this IF statement, CALCULATE the average between the two lowest blood sugar readings.
### PRINT the Average Blood Sugar reading in a formatted F-String.


def main () :
        ### PROMPT for mg/dL readings.
        bloodSugarA = int(input("Enter the first fasting blood sugar reading in mg/dL: "))
        bloodSugarB = int(input("Enter the second fasting blood sugar reading in mg/dL: "))
        bloodSugarC = int(input("Enter the third fasting blood sugar reading in mg/dL: "))

        ### EXCLUDE highest reading and calculate average.
        if bloodSugarA > bloodSugarB and bloodSugarA > bloodSugarC :
            totalBloodSugar = bloodSugarB + bloodSugarC
            averageBloodSugar = totalBloodSugar / 2
            
        elif bloodSugarB > bloodSugarA and bloodSugarB > bloodSugarC :
            totalBloodSugar = bloodSugarA + bloodSugarC
            averageBloodSugar = totalBloodSugar / 2
            
        elif bloodSugarC > bloodSugarA and bloodSugarC > bloodSugarB :
            totalBloodSugar = bloodSugarA + bloodSugarB
            averageBloodSugar = totalBloodSugar / 2

        ### PRINT average blood sugar in formatted f-string.
        print(f'The average blood sugar for this patient is {averageBloodSugar:.1f} mg/dL')

main () 
