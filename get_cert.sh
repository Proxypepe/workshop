#!/bin/bash

PASSIN=
PASSOUT=

log() {
    echo Created file: $1    
}

usage() {
    echo "Usage: $0 [arguments]"
}


if [[ ( $@ == "--help") ||  $@ == "-h" ]]; then 
	usage
	exit 0
fi 

if [  $# -le 1 ]; then 
    usage
    exit 1
fi 

# while getopts passin:passut: flag
# do
#     case "${flag}" in
#         passin) passin=${OPTARG};;
#         passut) passout=${OPTARG};;
#     esac
# done

# echo "passin: $passin";
# echo "passout: $passout";


# while getopts i:o: flag
# do
#     case "${flag}" in
#         i) PASSIN=${OPTARG};;
#         o) PASSOUT=${OPTARG};;
#     esac
# done
# echo "passin: $PASSIN";
# echo "passout: $PASSOUT";

while [[ $# -gt 0 ]]; do
  case $1 in    
        -i|--passin)
            PASSIN="$2"
            shift
            shift
            ;;
        -o|--passout)
            PASSOUT="$2"
            shift
            shift
            ;;
        -*|--*)
            echo "Unknown option $i"
            exit 1
            ;;
        *)
            usage
            ;;
  esac
done

echo "passin: $PASSIN";
echo "passout: $PASSOUT";
