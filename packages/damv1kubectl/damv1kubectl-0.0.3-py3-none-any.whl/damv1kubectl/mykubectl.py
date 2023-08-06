import re
import damv1env as env
import damv1time7 as time7
import damv1myparamikossh as prmko


class sanbox():
    
    def execsshcmd(self, _strcmd):
        oput = None # イニシャライズ
        try:
            if _strcmd.strip():
                srv = env.sandbox_srv # changes this for sandbox / production (  コンフィギュレーション )
                oput = prmko.sshcommand(srv.host._value_, srv.username._value_, srv.port._value_, srv.privatekey._value_, _strcmd, False)
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return oput  


    def getLst_info_allPods_by_ns(self, _ns):
        lst_po = [] # イニシャライズ
        try:
            cmd_gtpo = "kubectl get pods -n {0} --no-headers | awk {{'{1}'}} | column -t".format(_ns,'print $1"|"$3"|"$4"|"$5$6')
            lst_ipo = self.execsshcmd(cmd_gtpo)
            if len(lst_ipo)!=0:
                fdRow={}
                for row in lst_ipo:
                    sp_ipo = row.split('|')
                    fdRow = {   'name':sp_ipo[0],
                                'status':sp_ipo[1],
                                'restart':sp_ipo[2],
                                'age':sp_ipo[3] }
                    lst_po.append(fdRow)
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return lst_po

    def execCmd_by_regex_strquery(self, _strcmd, target_str=[]):
        oput = [] # イニシャライズ
        try:
            if _strcmd.strip():
                if len(target_str) !=0:
                    for target in target_str:
                        re_target = re.compile(r"({})".format(target), flags=re.IGNORECASE)
                        if re.search(re_target, _strcmd):
                            oput=self.execsshcmd(_strcmd) #  special objects スペシャルオブジェクト
                else:
                    oput=self.execsshcmd(_strcmd) # all objects すべてオブジェクト
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return oput 
    
    def getLst_log_pod_by_pattern_andTarget(self, _sincelast, _pod, _namespace, _pattern, _lst_target):
        lst_oput = [] # イニシャライズ
        try:
            query = f'kubectl logs --since={_sincelast} --timestamps=true {_pod} -n {_namespace} | grep "{_pattern}" | sort -k2 -r | head -n 1'
            lst_oput = self.execCmd_by_regex_strquery(query, _lst_target)
        except Exception as e:
            print(time7.currentTime7(),'Error Handling ( エラー ):',e)
        return lst_oput 










# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ## uncomments this bellow for testing only ( テスティング ) !
# # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# f = sanbox()
# def excute(_ns):
#     lst_po = []
#     print(time7.currentTime7(),'Begin ( はじまり )')
#     print(time7.currentTime7(),'(1) - Loading Process ( ローディング )')
#     lst_po = f.getLst_info_allPods_by_ns('sit')
#     print(lst_po)

# excute('sit')