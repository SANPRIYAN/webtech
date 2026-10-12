<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Book Inventory</h2>
                <table border="1" style="width:100%; border-collapse: collapse; text-align: left;">
                    <tr style="background-color: #f2f2f2;">
                        <th>Title</th>
                        <th>Author</th>
                        <th>Price</th>
                    </tr>
                    <xsl:for-each select="catalog/book">
                        <tr>
                            <td style="padding: 8px;">
                                <xsl:value-of select="title"/>
                            </td>
                            <td style="padding: 8px;">
                                <xsl:value-of select="author"/>
                            </td>
                            <td style="padding: 8px;">
                                <xsl:value-of select="price"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>