# Real Time File Aggregator - 

```shell
#!/bin/bash  
  
#This script is created for m2broker and pet feeds where the path gets converted to   
#the filename, if other feeds follow the same pattern, then this script will work for them as well.  
#Setting proxies to use aws cli commands from the script.  
set_proxy()  
{  
  export https_proxy="http://<ip>:8080/"  
  export http_proxy="http://<ip>:8080/"  
  export HTTPS_PROXY="http://<ip>:8080/"  
  export HTTP_PROXY="http://<ip>:8080/"  
  
  export no_proxy="*.s3.amazonaws.com,*.s3.us-east-1.amazonaws.com,*.s3.us-east-2.amazonaws.com,*.s3-us-west-1.amazonaws.com,*.s3-us-west-2.amazonaws.com,<ip2>,localhost,127.0.0.1,ip-*"  
  export NO_PROXY="*.s3.amazonaws.com,*.s3.us-east-1.amazonaws.com,*.s3.us-east-2.amazonaws.com,*.s3-us-west-1.amazonaws.com,*.s3-us-west-2.amazonaws.com,<ip2>,localhost,127.0.0.1,ip-*"  
}  
  
  
unset_proxy()  
{  
  export https_proxy=""  
  export http_proxy=""  
  export HTTPS_PROXY=""  
  export HTTP_PROXY=""  
  export no_proxy=""  
  export NO_PROXY=""  
}  
  
if [ $# -ne 4 ]  
then  
  echo "ERROR : Please pass proper number of parameters. {ENV} {CONFIG_FILE_PATH} {CLOUDWATCH_NAME\'s} {STEP_FN_NAME\'s}"  
  exit 1  
fi  
  
env=$1  
config_file_name=$2  
cloudwatch_names=$3  
step_fn_names=$4  
config_file=`echo ${config_file_name} | awk -F'/' '{print $NF}'`  
#config_file=$2  
  
if [[ "${env}" == "dev" ]]   
then  
    echo "dev env"  
	AWS_ACCNT_ID=<account_id>  
	kms_key_id="alias/S3/Dev-Component"  
	region="us-east-1"  
	echo $AWS_ACCNT_ID  
	stepfn_endpoint="https://vpce-<vpc_url>.states.us-east-1.vpce.amazonaws.com"  
	cw_endpoint="https://vpce-<vpc_url>.monitoring.us-east-1.vpce.amazonaws.com"  
elif [[ "${env}" == "uat" ]]   
then  
    echo "uat env"  
	AWS_ACCNT_ID=<account_id>  
	kms_key_id="alias/S3/Dev-Component"  
	region="us-east-1"  
	stepfn_endpoint="https://vpce-<vpc_url>.states.us-east-1.vpce.amazonaws.com"  
	cw_endpoint="https://vpce-<vpc_url>.monitoring.us-east-1.vpce.amazonaws.com"  
	echo $AWS_ACCNT_ID  
elif [[ "${env}" == "stg" ]]  
then  
    echo "stg env"  
	AWS_ACCNT_ID=<account_id>  
	kms_key_id="alias/S3/Staging-Component"  
	region="us-east-1"  
	stepfn_endpoint="https://vpce-<vpc_url>.states.us-east-1.vpce.amazonaws.com"  
	cw_endpoint="https://vpce-<vpc_url>.monitoring.us-east-1.vpce.amazonaws.com"  
	echo $AWS_ACCNT_ID  
elif [[ "${env}" == "prd" ]]  
then  
    echo "Prod env"  
    AWS_ACCNT_ID=<account_id>  
	kms_key_id="alias/S3/Prod-Component"  
    region="us-east-1"  
	stepfn_endpoint="https://<vpc_url>.states.us-east-1.vpce.amazonaws.com"  
	cw_endpoint="https://vpce-<vpc_url>.monitoring.us-east-1.vpce.amazonaws.com"  
	echo $AWS_ACCNT_ID  
elif [[ "${env}" == "dr" ]]  
then  
    echo "DR env"  
    AWS_ACCNT_ID=<account_id>  
	kms_key_id="alias/S3/Prod-Component"  
    region="eu-west-1"  
	stepfn_endpoint="https://<vpc_url>.states.us-east-1.vpce.amazonaws.com"  
	cw_endpoint="https://<vpc_url>.monitoring.us-east-1.vpce.amazonaws.com"  
	echo $AWS_ACCNT_ID  
	set_proxy()  
	{  
  	  export http_proxy='http://<url>:8080/'  
  	  export https_proxy='http://<url>:8080/'  
      export HTTPS_PROXY='http://<url>:8080/'  
      export HTTP_PROXY='http://<url>:8080/'  
  
      export no_proxy="*.s3.amazonaws.com,*.s3.us-east-1.amazonaws.com,*.s3.us-east-2.amazonaws.com,*.s3-us-west-1.amazonaws.com,*.s3-us-west-2.amazonaws.com,<ip2>,*.s3.eu-west-1.amazonaws.com,localhost,127.0.0.1,ip-*"  
      export NO_PROXY="*.s3.amazonaws.com,*.s3.us-east-1.amazonaws.com,*.s3.us-east-2.amazonaws.com,*.s3-us-west-1.amazonaws.com,*.s3-us-west-2.amazonaws.com,<ip2>,*.s3.eu-west-1.amazonaws.com,localhost,127.0.0.1,ip-*"  
	}  
fi  
  
script_home="/home/hadoop/real-time"  
s3_raw_bucket_platform="<s3_bucket_prefix>-raw"  
s3_raw_archive_bucket_platform="<s3_bucket_prefix>-raw-archive"  
s3_raw_bucket_partners="<s3_bucket_prefix>-partners-raw"  
s3_raw_archive_bucket_partners="<s3_bucket_prefix>-partners-raw-archive"  
  
  
lockfile="aggregator.lock"  
  
aws s3 ls s3://${s3_raw_archive_bucket_platform}/${lockfile}  
  
if [ $? -eq 0 ]  
then  
	echo "WARNING : An aggregator job is already running"  
	exit  
fi  
  
touch ${lockfile}  
aws s3 cp --sse aws:kms --sse-kms-key-id ${kms_key_id} ${lockfile} s3://${s3_raw_archive_bucket_platform}/  
  
rm -rf ${script_home}  
  
mkdir -p ${script_home}  
if [ $? -ne 0 ]  
then  
  echo "ERROR : Unable to create HOME DIR : ${script_home}"  
  exit 2  
fi  
  
cd ${script_home}  
aws s3 cp ${config_file_name} .  
if [ $? -ne 0 ]  
then  
  echo "ERROR : Unable to copy ${config_file} to HOME DIR : ${script_home}"  
  exit 2  
fi  
  
sudo yum install dos2unix -y  
dos2unix ${config_file}  
  
#set_proxy  
  
for i in ${cloudwatch_names//,/ }  
do  
    echo "$i"  
    # To disable the cloudwatch that reads the sqs and also trigger for step function.  
	echo "INFO : Disabling the ${i} cloudwatch rules."  
	aws events disable-rule --name ${i} --region ${region} --endpoint-url ${cw_endpoint}  
done  
  
for i in ${step_fn_names//,/ }  
do  
    echo "$i"  
	# To list the currently running step function.  
	output=`aws stepfunctions list-executions --state-machine-arn arn:aws:states:${region}:${AWS_ACCNT_ID}:stateMachine:${i} --status-filter RUNNING --endpoint-url ${stepfn_endpoint}`  
	if [ `echo "${output}" | grep "executionArn" | wc -l` -eq 1 ]  
	then  
  		executionArn=`echo "$output" | grep "executionArn" | awk '{print $2}' | sed 's/"//g'`  
  		echo "INFO : Aborting the step function ${i}"  
  		aws stepfunctions stop-execution --execution-arn ${executionArn} --endpoint-url ${stepfn_endpoint}  
  		sleep 10s  
	fi  
done  
  
#unset_proxy  
  
echo "INFO : Started reading the config file : ${config_file}"  
while read line  
do  
  folder=`echo ${line} | awk -F',' '{print $2}' | awk -F':' '{print $2}' | awk '{print $1}' | sed "s/'//g"`  
  msg_group_id=`echo ${line} | awk -F',' '{print $3}' | awk -F':' '{print $2}' | awk '{print $1}'| sed "s/'//g"`  
  path=`echo ${line} | awk -F',' '{print $4}' | awk -F':' '{print $2}' | awk '{print $1}'| awk -F'}' '{print $1}' | sed "s/'//g"`  
  is_partner=`echo ${line} | awk -F',' '{print $6}' | awk -F':' '{print $2}' | awk '{print $1}'| awk -F'}' '{print $1}' | sed "s/'//g"`  
    
  if [ $folder == "Feed" -a $msg_group_id == "MessageGroupId" -a $path == "S3location" ]  
  then  
    continue  
  fi  
    
  if [ -z ${is_partner} ]  
  then  
    s3_raw_bucket=${s3_raw_bucket_platform}  
    s3_raw_archive_bucket=${s3_raw_archive_bucket_platform}  
  elif [ ${is_partner} == 'Yes' ]  
  then  
    s3_raw_bucket=${s3_raw_bucket_partners}  
    s3_raw_archive_bucket=${s3_raw_archive_bucket_partners}  
  elif [ ${is_partner} == 'No' ]  
  then  
    s3_raw_bucket=${s3_raw_bucket_platform}  
    s3_raw_archive_bucket=${s3_raw_archive_bucket_platform}  
  fi  
    
  echo "---------------------------------------------------------------------------------------"  
  
  cd ${script_home}  
  mkdir -p ${folder}  
  cd ${folder}  
  if [ $? -ne 0 ]  
  then  
    echo "ERROR : Unable to change dir to : ${folder}"  
    break  
  fi  
  
  feed_name_regex=`echo ${path} | sed -e "s/\///g"`  
  feed_s3_tmp_path="s3://${s3_raw_bucket}/bluestreamraw/${path}"  
  feed_s3_path="s3://${s3_raw_bucket}/bluestream/${path}"  
  feed_s3_archive_path="s3://${s3_raw_archive_bucket}/bluestreamraw/${path}"  
    
  echo "INFO : Going to fetch and download txt files for : ${feed_name_regex}"  
  aws s3 cp ${feed_s3_tmp_path} . --exclude "*" --include "*.txt" --recursive  
    
  total_files=`ls | wc -l`  
    
  if [ ${total_files} -eq 0 ]  
  then  
    echo "INFO : No files for this feed."  
    echo "INFO : Going now to next path in config item."  
    cd ${script_home}  
    rm -rf ${folder}  
    continue  
  fi  
    
  echo "IMPORTANT INFO : GOING TO MERGE ${total_files} files into one."  
    
  ls > ${script_home}/filelist.txt  
    
  ts=`date +%Y%m%d%H%M%S`  
  final_feed_name=${feed_name_regex}_${ts}  
  
  echo "Now, merging the contents of all the files to create single file."  
    
  while read line  
  do  
    echo "reading file : ${line}"  
    cat ${line} >> ${final_feed_name}.data  
    echo "" >> ${final_feed_name}.data  
  done < ${script_home}/filelist.txt  
    
  if [ $? -ne 0 ]  
  then  
    echo "ERROR : Unable to merge all the content in one file. Please check."  
    break  
  fi  
  
  ffn_count=`cat ${final_feed_name}.data | awk /./ | wc -l`  
  ffn_size=`ls -ltr ${final_feed_name}.data | awk '{print $5}'`  
  ffn_path="${feed_s3_path}/${final_feed_name}.data"  
  
  echo "INFO : Creating the meta file for the merged data file."  
  echo -e "${ffn_path}\t1\t${ffn_count}\t${ffn_size}" > ${final_feed_name}.meta  
    
  echo "INFO : Uploading the data file : ${ffn_path}"  
  aws s3 cp --sse aws:kms --sse-kms-key-id ${kms_key_id} ${final_feed_name}.data ${ffn_path}  
  if [ $? -ne 0 ]  
  then  
    echo "ERROR : Unable to upload the data file to s3 raw bucket. Please check."  
    break  
  fi  
  
  echo "INFO : Uploading the meta file : ${feed_s3_path}/${final_feed_name}.meta"  
  aws s3 cp --sse aws:kms --sse-kms-key-id ${kms_key_id} ${final_feed_name}.meta ${feed_s3_path}/${final_feed_name}.meta   
  if [ $? -ne 0 ]  
  then  
    echo "ERROR : Unable to upload the meta file to s3 raw bucket. Please check."  
    break  
  fi  
  
  echo "INFO : Now deleting the contents on EMR of ${folder}"  
  cd ..  
  rm -rf ${script_home}/${folder}  
  if [ $? -ne 0 ]  
  then  
    echo "ERROR : Unable to delete the folder ${script_home}/${folder} . Please check."  
    break  
  fi  
    
  echo "INFO : Now archiving the txt files from ${feed_s3_tmp_path}."  
  aws s3 mv --sse aws:kms --sse-kms-key-id ${kms_key_id} --recursive ${feed_s3_tmp_path} ${feed_s3_archive_path}   
  if [ $? -ne 0 ]  
  then  
    echo "ERROR : Unable to archive the folder ${feed_s3_tmp_path} . Please check."  
  fi  
  
done < ${config_file}  
  
  
# To enable the cloudwatch that reads the sqs and also trigger for step function.  
#set_proxy  --removing proxy to use endpoint  
for i in ${cloudwatch_names//,/ }  
do  
    echo "$i"  
    echo "INFO : Enabling the ${i} cloudwatch rules."  
	aws events enable-rule --name ${i} --region ${region} --endpoint-url ${cw_endpoint}  
done  
#unset_proxy  
#to remove the aggregator lock  
aws s3 rm s3://${s3_raw_archive_bucket_platform}/${lockfile}  
  
```
