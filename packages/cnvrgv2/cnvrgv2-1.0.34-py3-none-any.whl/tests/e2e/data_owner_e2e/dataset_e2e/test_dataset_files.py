
from tests.e2e.data_owner_e2e.data_owner_files import DataOwnerFiles


class TestDatasetFiles(DataOwnerFiles):

    def test_put_files_success(self, e2e_dataset, temp_file):
        self.data_owner_put_files(e2e_dataset, temp_file)

    def test_put_unchanged_files_success(self, e2e_dataset, temp_file):
        self.data_owner_put_unchanged_files(e2e_dataset, temp_file)

    def test_put_folder_success(self, e2e_dataset, tmpdir):
        self.data_owner_put_folder(e2e_dataset, tmpdir)

    def test_put_files_override_false_success(self, e2e_dataset, temp_file):
        self.data_owner_put_files_override_false(e2e_dataset, temp_file)

    def test_put_files_override_true_success(self, e2e_dataset, temp_file):
        self.data_owner_put_files_override_true(e2e_dataset, temp_file)

    def test_list_files_success(self, e2e_dataset, tmpdir):
        self.data_owner_list_files(e2e_dataset, tmpdir)

    def test_list_files_and_folders_success(self, e2e_dataset, tmpdir):
        self.data_owner_list_files_and_folders(e2e_dataset, tmpdir)

    def test_delete_files_success(self, e2e_dataset, temp_file):
        self.data_owner_delete_files(e2e_dataset, temp_file)

    def test_clone_files_success(self, e2e_dataset, tmpdir):
        self.data_owner_clone_files(e2e_dataset, tmpdir)

    def test_clone_with_empty_folder_success(self, e2e_dataset, tmpdir):
        self.data_owner_clone_with_empty_folder(e2e_dataset, tmpdir)

    def test_upload_files_success(self, e2e_dataset, tmpdir):
        self.data_owner_upload_files(e2e_dataset, tmpdir)

    def test_upload_unchanged_files_success(self, e2e_dataset, tmpdir):
        self.data_owner_upload_unchanged_files(e2e_dataset, tmpdir)

    def test_upload_files_from_non_cnvrg_fails(self, e2e_dataset, tmpdir):
        self.data_owner_upload_files_from_non_cnvrg(e2e_dataset, tmpdir)

    def test_download_files_success(self, e2e_dataset):
        self.data_owner_download_files(e2e_dataset)

    def test_download_empty_folder_success(self, tmpdir, e2e_dataset):
        self.data_owner_download_empty_folder(e2e_dataset, tmpdir)

    def test_sync_local_success(self, e2e_dataset):
        self.data_owner_sync_local(e2e_dataset)

    def test_sync_local_with_output_success(self, e2e_dataset):
        self.data_owner_sync_local_with_output_dir(e2e_dataset)

    def test_put_files_absolute_path_success(self, tmpdir, e2e_dataset):
        self.data_owner_put_files_absolute_path(tmpdir, e2e_dataset)

    def test_remove_files_absolute_path_success(self, tmpdir, e2e_dataset):
        self.data_owner_remove_files_absolute_path(tmpdir, e2e_dataset)

    def test_remove_folders_through_upload_success(self, e2e_dataset, tmpdir):
        self.data_owner_remove_folders_through_upload(tmpdir, e2e_dataset)

    def test_remove_file_through_upload(self, e2e_dataset, tmpdir):
        self.data_owner_remove_file_through_upload(tmpdir, e2e_dataset)

    def test_remove_folder_locally_through_download_success(self, e2e_dataset, tmpdir):
        self.data_owner_remove_folder_locally_through_download(tmpdir, e2e_dataset)

    def test_remove_file_locally_through_download_success(self, e2e_dataset, tmpdir):
        self.data_owner_remove_file_locally_through_download(tmpdir, e2e_dataset)

    def test_data_owner_sync_complex(self, e2e_dataset, tmpdir):
        self.data_owner_sync_complex(tmpdir, e2e_dataset)

    def test_data_owner_nested(self, e2e_dataset, tmpdir):
        self.data_owner_nested(tmpdir, e2e_dataset)

    def test_data_owner_cache(self, e2e_dataset, tmpdir):
        self.data_owner_cache(tmpdir, e2e_dataset)

    def test_data_owner_sync_removed_file_success(self, e2e_dataset, tmpdir):
        self.data_owner_sync_removed_file(e2e_dataset, tmpdir)

    def test_data_owner_sync_removed_folder_success(self, e2e_dataset, tmpdir):
        self.data_owner_sync_removed_folder(e2e_dataset, tmpdir)

    def test_data_owner_verify_cnvrg_files_exists_success(self, e2e_dataset, tmpdir):
        self.data_owner_verify_cnvrg_files_exists(e2e_dataset, tmpdir)
