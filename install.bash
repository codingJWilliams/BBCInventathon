echo "Downlaoding files"
git clone https://github.com/codingJWilliams/BBCInventathon.git
cd BBCInventathon
rm -f todo.md
echo "You now need to go to makeymakey.com/remap/ and follow the instructions"
echo "Once you have done that connect the fruit to the makey makey then hit enter"
read enter
python3 setup.py
