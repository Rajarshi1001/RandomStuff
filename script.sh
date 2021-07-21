#! /bin/bash
name="Rajarshi Dutta"
echo my name is $name

read -p "Enter your name: " NAME
if [ $NAME == "Rishi" ]
then
    echo Hello $NAME , nice to meet ya
else
    echo your name is not $NAME, heheboi  
fi
FILE="samy.txt"
if [ -e $FILE ]
then
    echo $FILE is a file 
else
    echo $FILE is not a file
fi         
read -p "Are you studying in IITK" ans
case $ans in 
   [yY] | [yY][eE][sS])
    echo "Astro club is an exciting club, shoud try it out :)"
    ;;
   [nN] | [nN][oO])
    echo "Sorry you cant experience the Astro Club, better luck somewhere :/"
    ;;
   *)
   echo "Please enter either yes or no , dont stay dumb :)"
   ;;
esac
FILES=$(ls *.txt)
NEW=1
for FILE in $FILES
do
  echo "Renaming $FILE to new-$FILE"
  #rename file to new-filename
  mv $FILE $NEW.txt
  ((NEW++))
done     
mkdir hello
touch "hello/hw.txt"
echo "Hello,I am Rishi" >> "hello/hw.txt"
echo "file created xD"
