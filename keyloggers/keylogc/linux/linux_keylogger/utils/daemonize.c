int daemonize() {
	pid_t pid, sid;
	// fork off the parent process
	pid = fork();
	if (pid < 0) {
		exit(EXIT_FAILURE);
	}
	// exit parent process
	// child can continue to run after the parent has finished execution
	if (pid > 0) {
		exit(EXIT_SUCCESS);
	}
	// save files with permissions 007 (RWX for guest)
	umask(0);

	/* OPEN LOGS HERE */
	// create a new SID for the child process
	sid = setsid();
	if (sid < 0){
		exit(EXIT_FAILURE);
	}
	// change to root directory
	if ((chdir("/")) < 0) {
		exit(EXIT_FAILURE);
	}
	// close standard file descriptors to limit user interaction
	close(STDIN_FILENO);
	close(STDOUT_FILENO);
	close(STDERR_FILENO);

	return(pid);
}

