#!/bin/bash

NAMESPACE_WITH_REPORTS=($(kubectl get policyreport -A | awk ' NR > 1 { if ($4 > 1) print $1 ":" $2 }'))
REPORTS_DIRECTORY=reports

log () {
        echo namespace: $1 policy: $2 file path: $3
}

write_report() {
        kubectl get polr $2 -n $1 -o jsonpath='{.results[?(@.result=="fail")]}' | jq -s > $3
}

usage() {
    echo "Usage: $0 [arguments]"
}

if [[ ( $@ == "--help") ||  $@ == "-h" ]]; then
        usage
        exit 0
fi


while [[ $# -gt 0 ]]; do
  case $1 in
        -d|--dir)
            REPORTS_DIRECTORY="$2"
            shift
            shift
            ;;
        *)
            usage
            ;;
  esac
done



for i in "${NAMESPACE_WITH_REPORTS[@]}"; do
        NAMESPACE=${i%:*}
        POLICY=${i#*:}
        #if [ -d $REPORTS_DIRECTORY ]; then
        mkdir -p $REPORTS_DIRECTORY
        #fi
        FILE_NAME=$REPORTS_DIRECTORY/$NAMESPACE-$POLICY.json
        log $NAMESPACE $POLICY $FILE_NAME
        write_report $NAMESPACE $POLICY $FILE_NAME
done
