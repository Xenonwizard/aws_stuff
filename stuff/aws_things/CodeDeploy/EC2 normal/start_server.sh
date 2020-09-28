
#!/bin/bash
fuser -k 80/tcp
cd /home/ec2-user
chmod +x server
./server  >/dev/null 2>&1 &
