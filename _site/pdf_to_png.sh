FOLDER=${1}
Folders="$(ls -d ${FOLDER}*)"

for d in $Folders
do
Files="$(find $d -iname '*.pdf' | sort -r)"
for f in $Files
do

        convert -density 600 $f $d"/featured.png"
        
done
done