<?xml version="1.0" encoding="utf-8"?>
<!-- vim: set sts=2 sw=2: -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:param name="ext" select="'xml'"/>
  <xsl:output method="text"/>
  <xsl:template match="/mypy-report-index">
    <xsl:variable name="bad_lines" select="sum(file/@imprecise|file/@any)"/>
    <xsl:variable name="total_lines" select="sum(file/@total)"/>
    <xsl:variable name="total_sloc" select="$total_lines - sum(file/@empty)"/>
    <xsl:variable name="global_score" select="(1 - ($bad_lines div ($total_sloc + number($total_sloc = 0)))) * 10"/>
    <xsl:value-of select="format-number($global_score, '0.00')"/>
  </xsl:template>
</xsl:stylesheet>
