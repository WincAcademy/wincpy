if [ $CI ]
then
    cd $GITHUB_WORKSPACE
fi

pip install .

if [ $? != 0 ]
then
    echo "Could not find Wincpy in the current working directory."
    echo "Make sure you run this script from the top level of the repository."
fi

top_level=$PWD
solutions=$(find wincpy/solutions -mindepth 1 -maxdepth 1 -type d)
passed=true

for solution in $solutions
do
    cd $solution
    wincpy check > /dev/null 2>&1
    if [ $? == 2 ]
    then
        passed=false
        echo "$solution does not pass."
    fi
    cd $top_level
done

if [ $passed == false ]
then
    exit 1
fi
