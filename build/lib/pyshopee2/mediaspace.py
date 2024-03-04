from .base import BaseModule


class MediaSpace(BaseModule):

    def init_video_upload(self, **kwargs):
        """
        Initiate video upload session. Video duration should be between 10s and 60s (inclusive).
.
        :param kwargs:
        - file_md5 Required
        - file_size Required

        """
        return self.client.execute("media_space/init_video_upload", "POST", kwargs)

    def upload_video_part(self, **kwargs):
        """
        Upload video file by part using the upload_id in initiate_video_upload. The request Content-Type of this API should be of multipart/form-data
.
        :param kwargs:
         - video_upload_id Required
         - part_seq Required
         - content_md5 Required
         - part_content Required
        """
        return self.client.execute("media_space/upload_video_part", "POST", kwargs)

    def complete_video_upload(self, **kwargs):
        """
        Complete the video upload and starts the transcoding process when all parts are uploaded successfully.

        :param kwargs:
         - video_upload_id Required
         - part_seq_list Required
         - report_data Required
            - upload_cost Required

        """
        return self.client.execute("media_space/complete_video_upload", "POST", kwargs)

    def get_video_upload_result(self, **kwargs):
        """
        Query the upload status and result of video upload.

        :param kwargs:
        - video_upload_id Required
        """
        return self.client.execute("media_space/get_video_upload_result", "GET", kwargs)

    def cancel_video_upload(self, **kwargs):
        """
        Cancel a video upload session



        :param kwargs:
        - video_upload_id

        """
        return self.client.execute("media_space/cancel_video_upload", "POST", kwargs)

    def upload_image(self, **kwargs):
        """
        Upload image file.

        :param kwargs:
        - image Required
        """
        return self.client.execute("media_space/upload_image", "POST", kwargs)