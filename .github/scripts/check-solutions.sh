if [ $CI ]
then
    cd $GITHUB_WORKSPACE
fi

echo "Installing wincpy.."
pip install . > /dev/null

if [ $? != 0 ]
then
    echo "Could not find Wincpy in the current working directory."
    echo "Make sure you run this script from the top level of the repository."
fi

top_level=$PWD
solutions=$(find wincpy/solutions -mindepth 1 -maxdepth 1 -type d)
passed=true

echo "Running wincpy check on each solution.."
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
else
    echo "All solutions pass."
fi
