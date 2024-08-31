import threading
import multiprocessing as mp
import gymnasium as gym
from pokemonred_puffer.environment import RedGymEnv

class AsyncWrapper(gym.Wrapper):
    def __init__(self, env: RedGymEnv, send_queue: mp.Queue, recv_queue: mp.Queue):
        super().__init__(env)
        self.send_queue = send_queue
        self.recv_queue = recv_queue
        self.terminate_flag = threading.Event()  # To stop the thread gracefully
        print(f"Initialized queues for {self.env.unwrapped.env_id}")
        
        # Start the update thread
        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

    def update(self):
        while not self.terminate_flag.is_set():
            try:
                # Blocking call with timeout
                new_state = self.recv_queue.get(timeout=30)
                
                if new_state == "TERMINATE":
                    print(f"Terminating thread for {self.env.unwrapped.env_id}")
                    break
                elif new_state == b"":
                    print(f"Invalid state for {self.env.unwrapped.env_id}, skipping...")
                else:
                    # Reset the environment to the new state
                    self.env.unwrapped.update_state(new_state)
                    
                self.send_queue.put(self.env.unwrapped.env_id, timeout=300)  # Send acknowledgment

            except mp.queues.Empty:
                # print(f"Timeout waiting for state in {self.env.unwrapped.env_id}")
                pass
            except mp.queues.Full:
                # print(f"Timeout sending state in {self.env.unwrapped.env_id}")
                pass
            except Exception as e:
                print(f"Exception in thread for {self.env.unwrapped.env_id}: {e}")
                break

    def reset(self, seed=None, options=None):
        # Reset the environment
        return self.env.reset(seed=seed, options=options)

    def close(self):
        self.terminate_flag.set()  # Signal the thread to terminate
        self.recv_queue.put("TERMINATE")  # Ensure the thread exits the loop
        self.thread.join()  # Wait for the thread to finish
        print(f"Closed AsyncWrapper for {self.env.unwrapped.env_id}")

    def __del__(self):
        self.close()  # Ensure that the thread is properly closed when the object is deleted



# import threading
# from multiprocessing import Queue
# import gymnasium as gym

# from pokemonred_puffer.environment import RedGymEnv


# class AsyncWrapper(gym.Wrapper):
#     def __init__(self, env: RedGymEnv, send_queues: list[Queue], recv_queues: list[Queue]):
#         super().__init__(env)
#         self.send_queue = send_queues[self.env.unwrapped.env_id]
#         self.recv_queue = recv_queues[self.env.unwrapped.env_id]
#         print(f"Initialized queues for {self.env.unwrapped.env_id}")
#         # Now we will spawn a thread that will listen for updates
#         # and send back when the new state has been loaded
#         # this is a slow process and should rarely happen.
#         self.thread = threading.Thread(target=self.update, daemon=True)
#         self.thread.start()
#         # TODO: Figure out if there's a safe way to exit the thread

#     def update(self):
#         while True:
#             new_state = self.recv_queue.get()
#             if new_state == b"":
#                 print(f"invalid state for {self.env.unwrapped.env_id} skipping...")
#             else:
#                 self.env.unwrapped.update_state(new_state)
#             self.send_queue.put(self.env.unwrapped.env_id)
