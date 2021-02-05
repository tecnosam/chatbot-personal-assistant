# cleanest block
def clean_up(ds):
    src = ds['source'].to_list()
    msg = ds['msg'].to_list()
    new_x = []
    new_y = []
    for i in range( len(src) ):
        if (src[i] == 'me'):
            new_x.append( msg[i] ) # <---- the big difference
            for j in range( i , len(msg) ):
                print(i)
                if ( src[j] != 'me' ):
                    new_y.append( msg[j] )
                    break
            if ( len(new_x) != len(new_y) ):
                new_y.append(30000)
        # elif (src[i] != 'me'):
        #     new_y.append( msg[i] ) # <---- the big difference
        #     for j in range( i, len(msg) ):
        #         if ( src[j] == 'me' ):
        #             new_x.append( msg[j] )
        #             break
        #     if ( len(new_x) != len(new_y) ):
        #         new_x.append(20000)

    new_ds = pd.DataFrame({'x': new_x, 'y': new_y})
    return new_ds
# end

# ugliest block
def crawl_n_stash(ds):
    os.chdir( "static/models" )
    # cleaning up data
    ds = clean_up(ds)
    x = ds['x']
    y = ds['y']
    # fitting data
    cv = text.CountVectorizer().fit(x)
    td = text.TfidfTransformer( use_idf=False ).fit( cv.transform( x ) )
    X = td.transform( cv.transform( x ) )
    mod = mnb().fit(X, y)
    # dumping data
    jb.dump(td, "td.mod")
    jb.dump(cv, "cv.mod")
    jb.dump(mod, "model.mod")
    os.chdir( __PATH__ )
    return True
# end