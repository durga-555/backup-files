# importing all the  modules
import os
import shutil
import time

# main function which runs the program
def main():

	# initializing the count as zero
	deleted_folders_count = 0
	deleted_files_count = 0

	# specify the path 
	path = "E:/USER/AJITESH 2/WHITE HAT JR"

	# specify the number of days
	days = 30

	# converting days to seconds
	seconds = time.time() - (days * 24 * 60 * 60)

	# checking whether the file is present or not 
	if os.path.exists(path):

		# check all the folders
		for root_folder, folders, files in os.walk(path):

			# comparing 
			if seconds >= get_file_or_folder_age(root_folder):

				# removing the folders
				remove_folder(root_folder)
				deleted_folders_count += 1 # incrementing count

				# break and re-run
				break

			else:

				# checking folder from the root folder
				for folder in folders:

					# folder's path
					folder_path = os.path.join(root_folder, folder)

					# comparing with the number of days
					if seconds >= get_file_or_folder_age(folder_path):

						# call the remove folder functiom
						remove_folder(folder_path)
						deleted_folders_count += 1 # incrementing count


				# checking the files
				for file in files:

					# file path
					file_path = os.path.join(root_folder, file)

					# comparing the number of days
					if seconds >= get_file_or_folder_age(file_path):

						# call remove file function
						remove_file(file_path)
                        # increase the count
						deleted_files_count += 1 

		else:

			# if the path is not a directory
			# comparing with the days
			if seconds >= get_file_or_folder_age(path):

				# call the file
				remove_file(path)
				deleted_files_count += 1 # incrementing count

	else:

		# not found
		print(f'"{path}" is not found')
        # incriment count
		deleted_files_count += 1 

    # final message
	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")


def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the "+path)



def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print("Unable to delete the "+path)


def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime

# running the program
if __name__ == '__main__':
	main()