import threading
from app import app,listen_for_changes
from apscheduler.schedulers.background import BackgroundScheduler

def start_change_stream_thread():
    change_stream_thread = threading.Thread(target=listen_for_changes)
    change_stream_thread.daemon = True
    change_stream_thread.start()



def add_sched():
    sched = BackgroundScheduler(daemon=True)
    # sched.add_job(select_winner, 'interval', seconds=10)
    sched.start()

if __name__ == "__main__":
    start_change_stream_thread()
    add_sched()
    app.run(debug=True)