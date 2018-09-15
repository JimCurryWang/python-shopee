from .base import BaseModule


class Image(BaseModule):
    '''@@Significant OpenAPI Updates (2018-09-15/2018-??-??)
    '''

    def upload_image(self, **kwargs):
        """
        Use this optional API to pre-validate your image urls 
        and convert them to Shopee image url to use in item upload APIs.

        This way your potential invalid urls will not block your item upload process.

        :param kwargs:
            : images(string[]) - Image url. 
                                 max 2.0 MB each.Image format accepted: JPG, JPEG, PNG.
                                 Suggested dimension: 1024 x 1024 px.Max number of image is 9.
            >>> Example 
            >>> ["http://xxx.jpg"]

        :return:
            :images(object[])
                : image_url        - origin image url
                : shopee_image_url - Shopee image url
        """
        return self.client.execute("image/upload", "POST", kwargs)



