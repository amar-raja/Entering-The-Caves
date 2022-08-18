for text in $(head -n 100000 input.txt | grep "^")
do
curl -H "Content-Type: application/json" --request POST --data '{"teamname":"ANV","password":"anv@1998", "plaintext":"'"$text"'"}' -k https://students@172.27.26.188/
done > ciphertexts.txt